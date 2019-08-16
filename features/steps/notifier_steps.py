@then('I am notified \'{text}\'')
def step_impl(context, text):
    assert context.notifier.wasNotified(text) == True
