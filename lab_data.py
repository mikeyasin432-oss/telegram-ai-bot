# lab_data.py — extra lab knowledge topics
# Every entry automatically gets: a /command, a help button, and keyword matching.

EXTRA_KNOWLEDGE = {
    "hormones": {
        "title": "🧪 Hormone Assays",
        "content": (
            "<b>Reference Ranges</b>\n"
            "• Cortisol (8 AM): 5–25 µg/dL\n"
            "• Cortisol (midnight): &lt;5 µg/dL\n"
            "• Prolactin: M 4–15 / F 4–23 ng/mL\n"
            "• Testosterone: M 300–1000 / F 15–70 ng/dL\n"
            "• Estradiol: follicular 20–150 / peak 200–400 pg/mL\n"
            "• FSH: F follicular 3–12 / M 1–8 mIU/mL\n"
            "• LH: F follicular 2–12 / M 1–8 mIU/mL\n"
            "• hCG (non-pregnant): &lt;5 mIU/mL\n\n"
            "<b>Interpretation</b>\n"
            "• ↑ Cortisol + loss of diurnal rhythm → Cushing syndrome\n"
            "• ↓ Cortisol → Addison disease\n"
            "• ↑ Prolactin → prolactinoma, drugs\n"
            "• ↑ hCG → pregnancy, trophoblastic disease\n"
            "• ↑ FSH/LH + ↓ sex steroids → primary gonadal failure"
        ),
    },
    "cardiac": {
        "title": "❤️ Cardiac Markers",
        "content": (
            "<b>Reference Ranges</b>\n"
            "• Troponin I: &lt;0.04 ng/mL\n"
            "• Troponin T: &lt;0.01 ng/mL\n"
            "• CK-MB: &lt;5 ng/mL\n"
            "• BNP: &lt;100 pg/mL\n"
            "• NT-proBNP: &lt;125 pg/mL (under 75 yr)\n"
            "• Myoglobin: 25–72 ng/mL\n\n"
            "<b>Timing after MI</b>\n"
            "• Myoglobin rises 1–3 h\n"
            "• Troponin rises 3–6 h, peaks 12–24 h, stays 7–10 days\n"
            "• CK-MB rises 4–6 h, peaks 12–24 h, normal by 48–72 h"
        ),
    },
    "tumor_markers": {
        "title": "🎗️ Tumor Markers",
        "content": (
            "<b>Common Markers</b>\n"
            "• AFP: &lt;10 ng/mL — HCC, germ cell tumor\n"
            "• CEA: &lt;3 ng/mL — colorectal, lung, pancreas\n"
            "• PSA: &lt;4 ng/mL — prostate\n"
            "• CA-125: &lt;35 U/mL — ovarian\n"
            "• CA 19-9: &lt;37 U/mL — pancreatic\n"
            "• β-hCG: &lt;5 mIU/mL — trophoblastic tumor\n"
            "• CA 15-3: &lt;30 U/mL — breast\n\n"
            "<b>Key point</b>\n"
            "Tumor markers are for <i>monitoring</i>, not screening. "
            "They can be normal in cancer and elevated in benign disease."
        ),
    },
    "serology": {
        "title": "🦠 Serology & Immunology",
        "content": (
            "<b>Common Tests</b>\n"
            "• HIV Ag/Ab (4th gen) — screen\n"
            "• HBsAg, Anti-HBs, Anti-HBc — hepatitis B panel\n"
            "• Anti-HCV — hepatitis C screen\n"
            "• VDRL / RPR — syphilis screen (confirm with TPHA/FTA-ABS)\n"
            "• Widal — typhoid (limited sensitivity)\n"
            "• RF — rheumatoid factor\n"
            "• ASO — recent streptococcal infection\n"
            "• ANA — autoimmune screen\n\n"
            "<b>Interpretation</b>\n"
            "• Positive screen + positive confirm = infection\n"
            "• IgM = recent/acute; IgG = past or chronic"
        ),
    },
    "abg": {
        "title": "💨 Arterial Blood Gas",
        "content": (
            "<b>Normal Values</b>\n"
            "• pH: 7.35–7.45\n"
            "• PaCO₂: 35–45 mmHg\n"
            "• PaO₂: 80–100 mmHg\n"
            "• HCO₃⁻: 22–26 mmol/L\n"
            "• SaO₂: 95–100%\n"
            "• Base excess: −2 to +2\n\n"
            "<b>Quick Algorithm</b>\n"
            "1. pH &lt;7.35 = acidosis; &gt;7.45 = alkalosis\n"
            "2. PaCO₂ &gt;45 = respiratory acidosis\n"
            "3. PaCO₂ &lt;35 = respiratory alkalosis\n"
            "4. HCO₃⁻ &lt;22 = metabolic acidosis\n"
            "5. HCO₃⁻ &gt;26 = metabolic alkalosis"
        ),
    },
    "iron": {
        "title": "🩸 Iron Studies",
        "content": (
            "<b>Reference Ranges</b>\n"
            "• Serum iron: 50–150 µg/dL\n"
            "• Ferritin: M 30–300 / F 15–200 ng/mL\n"
            "• TIBC: 250–400 µg/dL\n"
            "• Transferrin saturation: 20–50%\n\n"
            "<b>Pattern Recognition</b>\n"
            "• Iron deficiency: ↓ ferritin, ↑ TIBC, ↓ saturation\n"
            "• Anemia of chronic disease: normal/↑ ferritin, ↓ TIBC\n"
            "• Hemochromatosis: ↑ ferritin, ↑ saturation (&gt;45%)"
        ),
    },
    "vitamins": {
        "title": "💊 Vitamin Assays",
        "content": (
            "<b>Reference Ranges</b>\n"
            "• Vitamin B12: 200–900 pg/mL\n"
            "• Folate: 3–17 ng/mL\n"
            "• 25-OH Vitamin D: 30–100 ng/mL (sufficient)\n"
            "• 20–29 = insufficient; &lt;20 = deficient\n\n"
            "<b>Deficiency Signs</b>\n"
            "• B12 deficiency: macrocytic anemia, neuropathy\n"
            "• Folate deficiency: macrocytic anemia (no neuropathy)\n"
            "• Vit D deficiency: rickets, osteomalacia"
        ),
    },
    "hemoglobinopathy": {
        "title": "🧬 Hemoglobinopathies",
        "content": (
            "<b>Sickle Cell Disease</b>\n"
            "• HbSS — sickle cell anemia\n"
            "• HbAS — sickle trait (usually asymptomatic)\n"
            "• Diagnosis: peripheral smear (sickle cells), "
            "sickling test, Hb electrophoresis\n\n"
            "<b>Thalassemia</b>\n"
            "• β-thal major: severe microcytic anemia, ↑ HbF\n"
            "• β-thal minor (trait): mild microcytosis, ↑ HbA₂\n"
            "• α-thal: deletional, ranges from silent to HbH disease\n\n"
            "<b>Lab Pattern</b>\n"
            "• Microcytic, target cells, Hb electrophoresis is definitive"
        ),
    },
    "malaria": {
        "title": "🦟 Malaria Diagnosis",
        "content": (
            "<b>Methods</b>\n"
            "• Thick film — detects parasites (sensitivity)\n"
            "• Thin film — species ID (P. falciparum vs others)\n"
            "• Rapid Diagnostic Test (RDT) — detects HRP-2, pLDH\n"
            "• PCR — species confirmation, mixed infections\n\n"
            "<b>Key Notes</b>\n"
            "• P. falciparum: multiple rings, banana-shaped gametocytes\n"
            "• P. vivax: Schüffner dots, enlarged RBCs\n"
            "• Repeat smears every 6–12 h if negative\n"
            "• HRP-2 RDT can stay positive 2–4 weeks after cure"
        ),
    },
    "tb": {
        "title": "🫁 Tuberculosis Diagnosis",
        "content": (
            "<b>Methods</b>\n"
            "• Sputum AFB smear (Ziehl-Neelsen) — 2 samples\n"
            "• GeneXpert MTB/RIF — detects TB + rifampicin resistance\n"
            "• Culture on LJ or MGIT — gold standard\n"
            "• TB LAMP — rapid molecular\n"
            "• IGRA — latent TB (not active)\n"
            "• Mantoux — latent TB screen\n\n"
            "<b>Interpretation</b>\n"
            "• AFB positive: smear-positive TB\n"
            "• GeneXpert RIF+ : drug-resistant TB\n"
            "• Culture takes 2–8 weeks"
        ),
    },
    "hepatitis": {
        "title": "🦠 Hepatitis Panel",
        "content": (
            "<b>Hepatitis B</b>\n"
            "• HBsAg + = active infection\n"
            "• Anti-HBs + = immune (vaccine or recovery)\n"
            "• Anti-HBc IgM = acute / recent\n"
            "• HBeAg + = high infectivity\n"
            "• HBV DNA = viral load\n\n"
            "<b>Hepatitis C</b>\n"
            "• Anti-HCV = screen (positive ≠ active)\n"
            "• HCV RNA = active infection (confirms)\n\n"
            "<b>Hepatitis A</b>\n"
            "• Anti-HAV IgM = acute; IgG = past/vaccinated"
        ),
    },
    "urine_culture": {
        "title": "🧫 Urine Culture",
        "content": (
            "<b>Significant Colony Count</b>\n"
            "• ≥10⁵ CFU/mL — significant bacteriuria\n"
            "• 10⁴–10⁵ CFU/mL — suspicious (repeat)\n"
            "• &lt;10⁴ CFU/mL — usually contamination\n\n"
            "<b>Common Pathogens</b>\n"
            "• E. coli (~80%)\n"
            "• Klebsiella, Proteus, Pseudomonas\n"
            "• Enterococcus, S. saprophyticus\n\n"
            "<b>Media</b>\n"
            "• CLED agar (yellow = lactose fermenter)\n"
            "• MacConkey agar\n"
            "• Blood agar"
        ),
    },
    "blood_culture": {
        "title": "💉 Blood Culture",
        "content": (
            "<b>Collection</b>\n"
            "• 2–3 sets (aerobic + anaerobic per set)\n"
            "• Before starting antibiotics\n"
            "• Different sites, 30 min apart\n"
            "• 10 mL blood per bottle for adults\n\n"
            "<b>Common Isolates</b>\n"
            "• S. aureus — bacteremia, endocarditis\n"
            "• Coagulase-negative Staph — common contaminant\n"
            "• E. coli, Klebsiella — gram-negative sepsis\n"
            "• Salmonella Typhi — typhoid\n"
            "• Strep pneumoniae — pneumonia sepsis"
        ),
    },
    "qc": {
        "title": "📊 Quality Control (QC)",
        "content": (
            "<b>Westgard Rules</b>\n"
            "• 1₂s — warning (one control &gt;2SD)\n"
            "• 1₃s — reject (one control &gt;3SD)\n"
            "• 2₂s — reject (two consecutive &gt;2SD, same side)\n"
            "• R₄s — reject (range &gt;4SD between two controls)\n"
            "• 4₁s — reject (four consecutive &gt;1SD, same side)\n"
            "• 10x — reject (ten consecutive on one side of mean)\n\n"
            "<b>Types</b>\n"
            "• Internal QC — daily, within-lab\n"
            "• External QC (EQA) — inter-laboratory comparison\n"
            "• Levey-Jennings chart — visualize trends"
        ),
    },
    "tdm": {
        "title": "💊 Therapeutic Drug Monitoring",
        "content": (
            "<b>Common Drugs</b>\n"
            "• Digoxin: 0.5–2.0 ng/mL\n"
            "• Vancomycin: trough 10–20 µg/mL (severe: 15–20)\n"
            "• Gentamicin: trough &lt;2 / peak 5–10 µg/mL\n"
            "• Phenytoin: 10–20 µg/mL\n"
            "• Carbamazepine: 4–12 µg/mL\n"
            "• Valproate: 50–100 µg/mL\n"
            "• Lithium: 0.6–1.2 mmol/L\n"
            "• Theophylline: 10–20 µg/mL\n\n"
            "<b>Timing matters</b> — trough before next dose"
        ),
    },
    "molecular": {
        "title": "🧬 Molecular Diagnostics",
        "content": (
            "<b>Common Techniques</b>\n"
            "• PCR — DNA amplification\n"
            "• RT-PCR — RNA (HIV viral load, SARS-CoV-2)\n"
            "• qPCR — quantitative\n"
            "• Multiplex PCR — multiple targets at once\n"
            "• LAMP — isothermal, rapid\n"
            "• GeneXpert — cartridge-based PCR\n"
            "• Sequencing — Sanger, NGS\n\n"
            "<b>Uses</b>\n"
            "• Viral loads (HIV, HBV, HCV)\n"
            "• TB + drug resistance\n"
            "• Genetic disease (sickle cell, thalassemia)\n"
            "• Oncology (mutation testing)"
        ),
    },
    "amylase": {
        "title": "🥔 Amylase & Lipase",
        "content": (
            "<b>Reference Ranges</b>\n"
            "• Amylase: 25–125 U/L\n"
            "• Lipase: 10–140 U/L\n\n"
            "<b>Interpretation</b>\n"
            "• Acute pancreatitis: amylase ↑ 3× ULN, lipase ↑ 3× ULN\n"
            "• Lipase more specific than amylase\n"
            "• Amylase rises 2–12 h, normal by 3–5 days\n"
            "• Lipase rises 4–8 h, stays 8–14 days\n"
            "• ↑ Amylase + normal lipase → salivary (mumps) or macroamylasemia"
        ),
    },
    "pregnancy": {
        "title": "🤰 Pregnancy Tests",
        "content": (
            "<b>hCG Reference</b>\n"
            "• Non-pregnant: &lt;5 mIU/mL\n"
            "• 3 weeks: 5–50\n"
            "• 4 weeks: 5–425\n"
            "• 5 weeks: 18–7,340\n"
            "• 6 weeks: 1,080–56,500\n"
            "• 8–10 weeks peak: 32,000–210,000\n\n"
            "<b>Patterns</b>\n"
            "• Doubles every 48–72 h in early viable pregnancy\n"
            "• Slow rise or fall → ectopic or non-viable\n"
            "• Very high → molar pregnancy\n\n"
            "<b>Also screened</b>: Rh, glucose, hemoglobin, HIV, HBsAg, syphilis"
        ),
    },
    "parasitology": {
        "title": "🪱 Parasitology",
        "content": (
            "<b>Common Parasites</b>\n"
            "• Ascaris lumbricoides — roundworm, eggs in stool\n"
            "• Entamoeba histolytica — amoebic dysentery (cysts/trophozoites)\n"
            "• Giardia lamblia — pear-shaped trophozoites\n"
            "• Hookworm — eggs in stool, iron-deficiency anemia\n"
            "• Strongyloides — larvae in stool\n"
            "• Schistosoma — eggs in urine (haematobium) or stool (mansoni)\n"
            "• Plasmodium — malaria (blood)\n\n"
            "<b>Methods</b>\n"
            "• Direct wet mount\n"
            "• Formol-ether concentration (most sensitive)\n"
            "• Kato-Katz (schistosomiasis, STH)"
        ),
    },
    "newborn": {
        "title": "👶 Newborn Screening",
        "content": (
            "<b>Common Conditions</b>\n"
            "• Congenital hypothyroidism (TSH)\n"
            "• Phenylketonuria (phenylalanine)\n"
            "• Congenital adrenal hyperplasia (17-OHP)\n"
            "• G6PD deficiency\n"
            "• Sickle cell disease (Hb electrophoresis)\n"
            "• Cystic fibrosis (immunoreactive trypsinogen)\n\n"
            "<b>Timing</b>\n"
            "• 24–72 h after birth (before discharge)\n"
            "• Repeat at 1–2 weeks if early discharge\n\n"
            "<b>Sample</b>\n"
            "• Heel-prick blood on filter paper (Guthrie card)"
        ),
    },
}
