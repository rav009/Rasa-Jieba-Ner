from typing import Any
from typing import Dict
from typing import Optional
from typing import Text

from rasa.nlu.extractors.extractor import EntityExtractor
from rasa.nlu.model import Metadata
from rasa.shared.nlu.training_data.training_data import Message
from rasa.shared.nlu.constants import (
    TEXT,
    ENTITIES
)
import jieba
import jieba.posseg as pseg

import copy


class JiebaNerExtractor(EntityExtractor):
    provides = ["entities"]

    defaults = {
        # nr：人名，ns：地名，nt：机构名, m: numbers
        "part_of_speech": ['nr'],
        "dictionary_path": None
    }

    def __init__(self, component_config=None):
        # type: (Optional[Dict[Text, Text]]) -> None
        super(JiebaNerExtractor, self).__init__(component_config)
        dictionary_path = self.component_config.get('dictionary_path')
        if dictionary_path is not None:
            jieba.load_userdict(dictionary_path)

    def process(self, message, **kwargs):
        # type: (Message, **Any) -> None
        entities = self.add_extractor_name(self.posseg_cut_examples(message))
        message.set(ENTITIES, message.get(ENTITIES, []) + entities, add_to_output=True)

    def posseg_cut_examples(self, example):
        raw_entities = []
        example_posseg = self.posseg(example.get(TEXT))
        for (item_posseg, start, end) in example_posseg:
            part_of_speech = self.component_config["part_of_speech"]
            for (word_posseg, flag_posseg) in item_posseg:
                if flag_posseg in part_of_speech:
                    raw_entities.append({
                        'start': start,
                        'end': end,
                        'value': word_posseg,
                        'entity': flag_posseg
                    })
        return raw_entities

    @staticmethod
    def posseg(text):
        result = []
        for (word, start, end) in jieba.tokenize(text):
            pseg_data = [(w, f) for (w, f) in pseg.cut(word)]
            result.append((pseg_data, start, end))
        return result

    @classmethod
    def load(cls,
             meta: Dict[Text, Any],
             model_dir=None,  # type: Optional[Text]
             model_metadata=None,  # type: Optional[Metadata]
             cached_component=None,  # type: Optional[Component]
             **kwargs
             ):
        return cls(meta)
