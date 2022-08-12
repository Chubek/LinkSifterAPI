
from .scoring import NERClass, NERScoreEntity


class NER:
    @staticmethod
    def calculate_ner(
        text: str, 
        context: str
    ) -> NERClass:
        score_entity = NERScoreEntity.new(text, context)

        return score_entity.assert_ner_class()
