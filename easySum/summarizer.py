from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.utils import get_stop_words

# algorithms
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.kl import KLSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.reduction import ReductionSummarizer
from sumy.summarizers.sum_basic import SumBasicSummarizer

from easySum.corpus import JapaneseCorpus


algorithm_dic = {"lex": LexRankSummarizer(), "tex": TextRankSummarizer(), "lsa": LsaSummarizer(),\
                 "kl": KLSummarizer(), "luhn": LuhnSummarizer(), "redu": ReductionSummarizer(),\
                 "sum": SumBasicSummarizer()}

LANGUAGE = 'japanese'


def summarize_sentences(sentences, sentences_count=3, algorithm="lex"):

    corpus_maker = JapaneseCorpus()


    preprocessed_sentences = corpus_maker.preprocessing(sentences)
    preprocessed_sentence_list = corpus_maker.make_sentence_list(preprocessed_sentences)
    corpus = corpus_maker.make_corpus()

    parser = PlaintextParser.from_string(' '.join(corpus), Tokenizer(LANGUAGE))

    # アルゴリズム選択
    try:
        summarizer = algorithm_dic[algorithm]
    except KeyError:
        print("algorithm name:'{}'is not found.".format(algorithm))

    summarizer.stop_words = get_stop_words(LANGUAGE)

    summary = summarizer(document=parser.document, sentences_count=sentences_count)

    return "".join([str(preprocessed_sentence_list[corpus.index(sentence.__str__())]) for sentence in summary])
