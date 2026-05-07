from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import HallucinationMetric

def test_legal_accuracy():
    metric = HallucinationMetric(threshold=0.5)
    test_case = LLMTestCase(
        input="What is the statute of limitations for fraud in New York?",
        actual_output="It is six years per CPLR 213(8).",
        context=["CPLR 213(8) states that fraud actions must be commenced within six years."]
    )
    assert_test(test_case, [metric])
