#Identify campaigns with low CTR (e.g., CTR < dataset median * 0.8 or config threshold).
#For each low-CTR campaign, sample top-performing creative messages across the dataset (by CTR/ROAS) and use template prompts to produce 6 diverse creative variants (headline, body, CTA).
#Output structured JSON with campaign_name, adset_name, creative_type, recommendations list.

from typing import Any, Dict, List

class CreativeGeneratorAgent:
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def generate(
        self,
        df,
        validated_insights: List[Dict[str, Any]],
        summaries: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        low_clusters = summaries.get("low_ctr_clusters", [])
        if not low_clusters:
            return []

        creatives: List[Dict[str, Any]] = []

        # Use account-level CTR for relative comparison
        overall_clicks = df["clicks"].sum()
        overall_impr = df["impressions"].sum()
        account_ctr = float(overall_clicks / overall_impr) if overall_impr > 0 else 0.0

        for row in low_clusters[:3]:
            ctr = row["ctr"]
            roas = row["roas"]
            delta_pct = (
                (ctr - account_ctr) / account_ctr * 100.0 if account_ctr > 0 else 0.0
            )

            cluster_id = f"{row['campaign_name']} | {row['adset_name']}"
            problem = (
                f"CTR {ctr*100:.2f}% (~{abs(delta_pct):.0f}% below account average) and "
                f"ROAS {roas:.2f} with spend {row['spend']:.0f}."
            )

            # Simple heuristic: women vs men
            name_lower = row["campaign_name"].lower()
            if "women" in name_lower:
                angle = "Fit anxiety + invisibility + everyday confidence"
                headlines = [
                    "No lines. No digging. Just an everyday bra you forget you're wearing.",
                    "Your T-shirt bra that never shows up in photos.",
                    "One bra for work, errands, and nights out.",
                ]
                bodies = [
                    "If your current bra leaves lines on every tee, switch to a seamless fit that stays invisible under even the clingiest tops.",
                    "Stop choosing outfits around your bra. Our seamless, wire-free design stays smooth under tees, shirts, and dresses — all day.",
                    "Straps that don’t dig, cups that don’t gap, and a back that doesn’t roll. This is the everyday bra you can actually forget about.",
                ]
                ctas = [
                    "Find Your Seamless Fit",
                    "Upgrade Your Everyday Bra",
                    "Shop Invisible Bras",
                ]
            else:
                angle = "Pain-point first + stay-put comfort"
                headlines = [
                    "Tired of boxers that ride up? Meet the no-adjust boxer.",
                    "No more pinch lines. Just smooth, stay-put boxers.",
                    "9/10 men switch after one wear — stay-put comfort boxers.",
                ]
                bodies = [
                    "If your current boxers bunch, twist, and ride up, it's time to upgrade. Our stay-put waistband and anti-chafe fabric keep everything where it should be — even on long days.",
                    "Office, gym, or travel — one boxer that doesn’t roll, pinch, or dig. Try our stay-put boxers with a comfort guarantee.",
                    "Join men who switched to boxers that don’t need constant fixing. Breathable, stay-put, and built for all-day movement.",
                ]
                ctas = [
                    "Shop Stay-Put Boxers",
                    "Try the No-Adjust Boxer",
                    "Upgrade Your Everyday",
                ]

            creatives.append(
                {
                    "cluster_id": cluster_id,
                    "problem": problem,
                    "current_examples": [],
                    "diagnosis": [
                        "CTR is substantially below account average, indicating weak thumb-stop rate.",
                        "Messaging likely leans on generic comfort/invisibility without clear problem or proof.",
                    ],
                    "recommendations": {
                        "angle": angle,
                        "headline_variants": headlines,
                        "primary_text_variants": bodies,
                        "cta_variants": ctas,
                    },
                }
            )

        return creatives
