from .models import PillarScore, Match, Quote, Recommendation, DimensionScore, Assessment

def save_assessment_data(assessment_id, response_data):
    assessment = Assessment.objects.get(id=assessment_id)
    print(f"jkfjkj jkjkj jkjkjk ")
    # Pillar Scores
    for pillar, score in response_data.get('pillar_scores', {}).items():
        PillarScore.objects.create(assessment=assessment, pillar=pillar, score=score)

    # Matches
    for match in response_data.get('matches', []):
        Match.objects.create(
            assessment=assessment,
            pillar=match['pillar'],
            matched_phrase=match['matched_phrase'],
            input_phrase=match['input_phrase'],
            score=match['score']
        )

    # Dimension Scores
    for dimension, score in response_data.get('dimension_scores', {}).items():
        DimensionScore.objects.create(
            assessment=assessment,
            dimension=dimension,
            score=score
        )

    # Quotes & Recommendations
    for pillar, content in response_data.get('recommendations', {}).items():
        for quote in content.get('quotes', []):
            Quote.objects.create(assessment=assessment, pillar=pillar, quote_text=quote)
        for rec in content.get('recommendations', []):
            Recommendation.objects.create(assessment=assessment, pillar=pillar, recommendation_text=rec)

    # Optional: Update maturity level again if needed
    assessment.maturity_level = response_data.get('maturity_level', 'Emerging')
    assessment.save()

# touched on 2025-05-27T15:28:59.284746Z
# touched on 2025-08-14T21:16:24.128433Z
# touched on 2025-08-14T21:17:28.540384Z
# touched on 2025-08-14T21:17:39.021524Z
# touched on 2025-08-14T21:17:51.595704Z
# touched on 2025-08-14T21:17:59.880759Z
# touched on 2025-08-14T21:18:16.428803Z
# touched on 2025-08-14T21:18:28.902914Z
# touched on 2025-08-14T21:18:32.927691Z
# touched on 2025-08-14T21:18:58.069717Z
# touched on 2025-08-14T21:19:02.236994Z
# touched on 2025-08-14T21:19:04.389026Z
# touched on 2025-08-14T21:19:12.728775Z
# touched on 2025-08-14T21:19:21.325677Z
# touched on 2025-08-14T21:19:25.418726Z
# touched on 2025-08-14T21:19:46.351307Z
# touched on 2025-08-14T21:19:51.317555Z
# touched on 2025-08-14T21:19:53.437850Z
# touched on 2025-08-14T21:20:04.568816Z
# touched on 2025-08-14T21:20:06.948364Z
# touched on 2025-08-14T21:20:11.101211Z
# touched on 2025-08-14T21:20:15.184212Z
# touched on 2025-08-14T21:20:17.539382Z