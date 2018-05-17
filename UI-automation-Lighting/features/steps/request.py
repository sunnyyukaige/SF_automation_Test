from behave import *

use_step_matcher("re")

@then('I can get privilege of user "\{userid\}"')
def step_impl(context,userid):
    assert userid==37


@then('I can get privilege of user "17"')
def step_impl(context,userid):
    """
    :type context: behave.runner.Context
    """
    pass