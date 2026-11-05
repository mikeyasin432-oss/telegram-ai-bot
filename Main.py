import re
import os
import html
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()

# ================= KNOWLEDGE BASE =================
KNOWLEDGE = {{# ---- Merge external topics from lab_data.py if present ----
try:
    from lab_data import EXTRA_KNOWLEDGE
    KNOWLEDGE.update(EXTRA_KNOWLEDGE)
    logger.info(f"Loaded {len(EXTRA_KNOWLEDGE)} extra topics from lab_data.py")
except ImportError:}
    logger.info("lab_data.py not found — using base topics only")
    "cbc": {
        "title": "🩸 Complete Blood Count (CBC)",
        "content": (
            "<b>Reference Ranges (Adults)</b>\n"
            "• WBC: 4.0–11.0 ×10⁹/L\n"
            "• RBC: M 4.5–5.9 / F 4.1–5.1 ×10¹²/L\n"
            "• Hemoglobin: M 13.5–17.5 / F 12.0–15.5 g/dL\n"
            "• Hematocrit: M 41–53% / F 36–46%\n"
            "• MCV: 80–100 fL\n"
            "• MCH: 27–33 pg\n"
            "• MCHC: 32–36 g/dL\n"
            "• Platelets: 150–450 ×10⁹/L\n\n"
            "<b>Key Interpretations</b>\n"
            "• Low Hb → anemia\n"
            "• High WBC → infection / inflammation / leukemia\n"
            "• Low platelets → thrombocytopenia (bleeding risk)\n"
            "• High MCV → B12/folate deficiency, alcohol\n"
            "• Low MCV → iron deficiency, thalassemia"
        ),
    },
    "urinalysis": {
        "title": "🧪 Urinalysis",
        "content": (
            "<b>Normal Findings</b>\n"
            "• Color: yellow–amber\n• Clarity: clear\n"
            "• pH: 4.5–8.0\n• Specific gravity: 1.005–1.030\n"
            "• Protein / Glucose / Ketones / Blood: negative\n"
            "• Nitrite / Leukocyte esterase / Bilirubin: negative\n\n"
            "<b>Common Abnormalities</b>\n"
            "• Proteinuria → renal disease, pre-eclampsia\n"
            "• Glycosuria → diabetes mellitus\n"
            "• Hematuria → UTI, stones, trauma, glomerulonephritis\n"
            "• Nitrite + LE → bacterial UTI\n"
            "• Ketones → DKA, starvation"
        ),
    },
    "lft": {
        "title": "🧬 Liver Function Tests (LFT)",
        "content": (
            "<b>Reference Ranges</b>\n"
            "• ALT: 7–56 U/L\n• AST: 10–40 U/L\n"
            "• ALP: 44–147 U/L\n• GGT: M 8–61 / F 5–36 U/L\n"
            "• Total bilirubin: 0.1–1.2 mg/dL\n"
            "• Direct bilirubin: 0.0–0.3 mg/dL\n"
            "• Total protein: 6.0–8.3 g/dL\n• Albumin: 3.5–5.5 g/dL\n\n"
            "<b>Interpretation</b>\n"
            "• ↑ ALT/AST → hepatocellular injury\n"
            "• ↑ ALP/GGT → cholestasis\n"
            "• ↑ Direct bilirubin → post-hepatic obstruction\n"
            "• ↓ Albumin → chronic liver disease / malnutrition"
        ),
    },
    "rft": {
        "title": "🧫 Renal Function Tests (RFT)",
        "content": (
            "<b>Reference Ranges</b>\n"
            "• Urea (BUN): 7–20 mg/dL (2.5–7.1 mmol/L)\n"
            "• Creatinine: M 0.7–1.3 / F 0.6–1.1 mg/dL\n"
            "• eGFR: &gt;90 mL/min/1.73m² (normal)\n"
            "• Uric acid: M 3.4–7.0 / F 2.4–6.0 mg/dL\n\n"
            "<b>Interpretation</b>\n"
            "• ↑ Urea &amp; Creatinine → impaired renal function\n"
            "• BUN:Cr ratio &gt;20:1 → pre-renal (dehydration)\n"
            "• ↓ eGFR → CKD staging\n"
            "• ↑ Uric acid → gout, tumor lysis"
        ),
    },
    "glucose": {
        "title": "🩸 Glucose &amp; Diabetes Tests",
        "content": (
            "<b>Reference Ranges</b>\n"
            "• Fasting glucose: 70–99 mg/dL\n"
            "• Random glucose: &lt;140 mg/dL\n"
            "• HbA1c: &lt;5.7% normal; 5.7–6.4% prediabetes; ≥6.5% diabetes\n"
            "• OGTT (2 hr): &lt;140 normal; 140–199 IGT; ≥200 diabetes\n\n"
            "<b>ADA Diagnostic Criteria</b>\n"
            "• FPG ≥126 mg/dL\n• 2-h OGTT ≥200 mg/dL\n"
            "• HbA1c ≥6.5%\n• Random ≥200 mg/dL with symptoms"
        ),
    },
    "lipid": {
        "title": "🧪 Lipid Profile",
        "content": (
            "<b>Reference Ranges</b>\n"
            "• Total cholesterol: &lt;200 mg/dL (desirable)\n"
            "• LDL: &lt;100 mg/dL (optimal)\n"
            "• HDL: &gt;40 M / &gt;50 F mg/dL\n"
            "• Triglycerides: &lt;150 mg/dL\n\n"
            "<b>Interpretation</b>\n"
            "• ↑ LDL → atherosclerosis risk\n"
            "• ↓ HDL → cardiovascular risk\n"
            "• ↑ TG → pancreatitis risk, metabolic syndrome"
        ),
    },
    "thyroid": {
        "title": "🦋 Thyroid Function Tests",
        "content": (
            "<b>Reference Ranges</b>\n"
            "• TSH: 0.4–4.0 mIU/L\n"
            "• Free T4: 0.8–1.8 ng/dL\n"
            "• Free T3: 2.3–4.2 pg/mL\n\n"
            "<b>Interpretation</b>\n"
            "• ↑ TSH + ↓ FT4 → primary hypothyroidism\n"
            "• ↓ TSH + ↑ FT4 → hyperthyroidism\n"
            "• ↓ TSH + ↓ FT4 → central hypothyroidism"
        ),
    },
    "coag": {
        "title": "🩸 Coagulation Profile",
        "content": (
            "<b>Reference Ranges</b>\n"
            "• PT: 11–13.5 sec\n• INR: 0.8–1.1\n"
            "• APTT: 25–35 sec\n• Fibrinogen: 200–400 mg/dL\n"
            "• D-dimer: &lt;500 ng/mL FEU\n\n"
            "<b>Interpretation</b>\n"
            "• ↑ PT/INR → warfarin, liver disease, vit K deficiency\n"
            "• ↑ APTT → heparin, hemophilia, vWD\n"
            "• ↑ D-dimer → DVT/PE, DIC"
        ),
    },
    "electrolytes": {
        "title": "⚗️ Electrolyte Panel",
        "content": (
            "<b>Reference Ranges</b>\n"
            "• Sodium: 135–145 mmol/L\n• Potassium: 3.5–5.0 mmol/L\n"
            "• Chloride: 98–107 mmol/L\n• Bicarbonate: 22–26 mmol/L\n"
            "• Calcium: 8.5–10.5 mg/dL\n• Magnesium: 1.7–2.2 mg/dL\n"
            "• Phosphate: 2.5–4.5 mg/dL\n\n"
            "<b>Critical Values</b>\n"
            "• K⁺ &lt;2.5 or &gt;6.5 mmol/L — life-threatening\n"
            "• Na⁺ &lt;120 or &gt;160 mmol/L — urgent"
        ),
    },
    "csf": {
        "title": "🧫 Cerebrospinal Fluid (CSF)",
        "content": (
            "<b>Normal Findings</b>\n"
            "• Appearance: clear, colorless\n• WBC: 0–5 cells/µL\n"
            "• Protein: 15–45 mg/dL\n"
            "• Glucose: 50–80 mg/dL (≈60% of serum)\n"
            "• Lactate: &lt;2.1 mmol/L\n\n"
            "<b>Pattern Recognition</b>\n"
            "• Bacterial: ↑↑ WBC (neutrophils), ↑ protein, ↓ glucose\n"
            "• Viral: ↑ WBC (lymphocytes), normal glucose\n"
            "• TB: ↑ WBC (lymphocytes), ↑ protein, ↓ glucose"
        ),
    },
    "micro": {
        "title": "🔬 Microbiology Essentials",
        "content": (
            "<b>Gram Stain</b>\n"
            "• Gram-positive → purple (thick peptidoglycan)\n"
            "• Gram-negative → pink/red (thin peptidoglycan)\n\n"
            "<b>Common Media</b>\n"
            "• Blood agar — general, hemolysis\n"
            "• MacConkey — gram-negative, lactose fermentation\n"
            "• Chocolate agar — fastidious (H. influenzae)\n"
            "• CLED — urine culture\n"
            "• Mannitol salt — Staphylococcus\n\n"
            "<b>Quick Tests</b>\n"
            "• Catalase, coagulase, oxidase, urease\n"
            "• Indole, citrate, TSI"
        ),
    },
    "bloodbank": {
        "title": "💉 Blood Bank Essentials",
        "content": (
            "<b>ABO System</b>\n"
            "• A: A antigen, anti-B\n• B: B antigen, anti-A\n"
            "• AB: A &amp; B antigens, no antibodies (universal recipient)\n"
            "• O: no antigens, anti-A &amp; anti-B (universal RBC donor)\n\n"
            "<b>Rh Factor</b>\n"
            "• Rh+ (D antigen present) — most common\n"
            "• Rh− can develop anti-D if exposed\n\n"
            "<b>Crossmatch</b>\n"
            "• Major: recipient serum + donor cells\n"
            "• Minor: donor serum + recipient cells\n\n"
            "<b>Components</b>\n"
            "• PRBC, FFP, platelets, cryoprecipitate"
        ),
    },
    "stool": {
        "title": "🧪 Stool Analysis",
        "content": (
            "<b>Normal Findings</b>\n"
            "• Color: brown\n• Consistency: formed\n"
            "• Occult blood: negative\n• WBC/RBC: none\n"
            "• Parasites/ova: none\n\n"
            "<b>Common Findings</b>\n"
            "• Bloody diarrhea + WBC → invasive bacterial infection\n"
            "• Ova/cysts → parasitic infection (Giardia, Entamoeba, Ascaris)\n"
            "• Fat globules → malabsorption\n"
            "• ↑ fecal calprotectin → IBD"
        ),
    },
    "semen": {
        "title": "🧬 Semen Analysis (WHO 5th ed.)",
        "content": (
            "<b>Reference Values</b>\n"
            "• Volume: ≥1.5 mL\n• Concentration: ≥15 million/mL\n"
            "• Total sperm: ≥39 million/ejaculate\n"
            "• Total motility: ≥40%\n• Progressive motility: ≥32%\n"
            "• Normal morphology: ≥4%\n• pH: ≥7.2\n\n"
            "<b>Interpretation</b>\n"
            "• Oligozoospermia: &lt;15 million/mL\n"
            "• Azoospermia: no sperm\n"
            "• Asthenozoospermia: reduced motility\n"
            "• Teratozoospermia: abnormal morphology"
        ),
    },
}


def format_message(key: str) -> str:
    entry = KNOWLEDGE[key]
    return f"<b>{entry['title']}</b>\n\n{entry['content']}"


# ================= HANDLERS =================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name or "there"
    await update.message.reply_text(
        f"👋 Hello <b>{html.escape(name)}</b>!\n\n"
        "I'm <b>MLS Bot</b> — your Medical Laboratory Science assistant.\n\n"
        "Use /help to see all topics, or just type a keyword like <i>anemia</i>, "
        "<i>creatinine</i>, or <i>hba1c</i>.",
        parse_mode="HTML",
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🩸 CBC", callback_data="cbc"),
         InlineKeyboardButton("🧪 Urinalysis", callback_data="urinalysis")],
        [InlineKeyboardButton("🧬 LFT", callback_data="lft"),
         InlineKeyboardButton("🧫 RFT", callback_data="rft")],
        [InlineKeyboardButton("🩸 Glucose", callback_data="glucose"),
         InlineKeyboardButton("🧪 Lipid", callback_data="lipid")],
        [InlineKeyboardButton("🦋 Thyroid", callback_data="thyroid"),
         InlineKeyboardButton("🩸 Coagulation", callback_data="coag")],
        [InlineKeyboardButton("⚗️ Electrolytes", callback_data="electrolytes"),
         InlineKeyboardButton("🧫 CSF", callback_data="csf")],
        [InlineKeyboardButton("🔬 Microbiology", callback_data="micro"),
         InlineKeyboardButton("💉 Blood Bank", callback_data="bloodbank")],
        [InlineKeyboardButton("🧪 Stool", callback_data="stool"),
         InlineKeyboardButton("🧬 Semen", callback_data="semen")],
    ]
    await update.message.reply_text(
        "📚 <b>Medical Laboratory Science Topics</b>\n\n"
        "Tap a button or use commands:\n"
        "/cbc /urinalysis /lft /rft /glucose /lipid /thyroid /coag\n"
        "/electrolytes /csf /micro /bloodbank /stool /semen\n\n"
        "/search &lt;term&gt; — search the knowledge base\n"
        "/about — about this bot",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ <b>About MLS Bot</b>\n\n"
        "A Medical Laboratory Science reference bot built with python-telegram-bot.\n\n"
        "📌 <i>Disclaimer: For educational purposes only. Not a substitute for "
        "professional medical advice or interpretation by a licensed laboratory professional.</i>",
        parse_mode="HTML",
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    key = query.data
    if key in KNOWLEDGE:
        await query.message.reply_text(format_message(key), parse_mode="HTML")
    else:
        await query.message.reply_text("Unknown topic.")


def make_handler(key: str):
    async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            await update.message.reply_text(format_message(key), parse_mode="HTML")
        except Exception as e:
            logger.exception(e)
            await update.message.reply_text("⚠️ Error fetching information.")
    return handler


async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /search <term>\nExample: /search anemia")
        return
    term = " ".join(context.args).lower()
    safe_term = html.escape(term)
    matches = [
        k for k, v in KNOWLEDGE.items()
        if term in v["title"].lower() or term in v["content"].lower()
    ]
    if not matches:
        await update.message.reply_text(
            f"No results for '<b>{safe_term}</b>'.", parse_mode="HTML"
        )
        return
    lines = [f"🔍 <b>Results for '{safe_term}'</b>\n"]
    for m in matches:
        lines.append(f"• /{m} — {KNOWLEDGE[m]['title']}")
    await update.message.reply_text("\n".join(lines), parse_mode="HTML")


async def unknown_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (update.message.text or "").lower()
    keyword_map = {
        "cbc": "cbc", "blood count": "cbc", "hemoglobin": "cbc",
        "anaemia": "cbc", "anemia": "cbc", "wbc": "cbc", "platelet": "cbc",
        "urine": "urinalysis", "urinalysis": "urinalysis",
        "liver": "lft", "alt": "lft", "ast": "lft", "bilirubin": "lft",
        "kidney": "rft", "creatinine": "rft", "urea": "rft", "egfr": "rft",
        "glucose": "glucose", "sugar": "glucose", "diabetes": "glucose",
        "hba1c": "glucose", "ogtt": "glucose",
        "cholesterol": "lipid", "lipid": "lipid", "triglyceride": "lipid",
        "ldl": "lipid", "hdl": "lipid",
        "thyroid": "thyroid", "tsh": "thyroid", "t3": "thyroid", "t4": "thyroid",
        "coag": "coag", "pt": "coag", "aptt": "coag", "inr": "coag",
        "d-dimer": "coag", "fibrinogen": "coag",
        "electrolyte": "electrolytes", "sodium": "electrolytes",
        "potassium": "electrolytes", "calcium": "electrolytes",
        "csf": "csf", "spinal": "csf", "meningitis": "csf",
        "micro": "micro", "culture": "micro", "gram": "micro",
        "bacteria": "micro", "media": "micro",
        "blood bank": "bloodbank", "blood group": "bloodbank",
        "crossmatch": "bloodbank", "abo": "bloodbank", "rh": "bloodbank",
        "stool": "stool", "feces": "stool", "parasite": "stool",
        "semen": "semen", "sperm": "semen",
    }
    for keyword, key in keyword_map.items():
        if keyword in text:
            await update.message.reply_text(format_message(key), parse_mode="HTML")
            return
    await update.message.reply_text(
        "🤔 I didn't understand that. Try /help to see available topics."
    )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error("Exception while handling update:", exc_info=context.error)
    try:
        if isinstance(update, Update) and update.effective_message:
            await update.effective_message.reply_text(
                "⚠️ Something went wrong. Please try again."
            )
    except Exception:
        pass


# ================= MAIN =================

def main():
    if not BOT_TOKEN or BOT_TOKEN == "PASTE_YOUR_TOKEN_HERE":
        raise SystemExit("ERROR: BOT_TOKEN environment variable is not set.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Core commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("search", search_command))

    # One command per topic
    for key in KNOWLEDGE.keys():
        app.add_handler(CommandHandler(key, make_handler(key)))

    # Inline keyboard + free-text fallback + errors
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_text))
    app.add_error_handler(error_handler)

    logger.info("MLS Bot is polling...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
