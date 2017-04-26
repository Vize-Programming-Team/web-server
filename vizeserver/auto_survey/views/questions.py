from django.core.urlresolvers import reverse
from twilio.twiml.messaging_response import MessagingResponse
from django.http import HttpResponse

from auto_survey.models import Question
from django.views.decorators.http import require_GET


@require_GET
def show_question(request, survey_id, question_id):
    question = Question.objects.get(id=question_id)

    twiml = sms_question(question)

    request.session['answering_question_id'] = question.id
    return HttpResponse(twiml, content_type='application/xml')


def sms_question(question):
    twiml_response = MessagingResponse()

    twiml_response.message(question.body)
    twiml_response.message(SMS_INSTRUCTIONS[question.kind])

    return twiml_response

SMS_INSTRUCTIONS = {
    Question.TEXT: 'Please type your answer',
    Question.YES_NO: 'Please type 1 for yes and 0 for no',
    Question.NUMERIC: 'Please type a number between 1 and 10'
}


def save_response_url(question):
    return reverse('save_response',
                   kwargs={'survey_id': question.survey.id,
                           'question_id': question.id})