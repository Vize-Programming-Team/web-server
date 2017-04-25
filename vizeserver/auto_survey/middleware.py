class SMSMiddleware(object):

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        args = request.POST or request.GET
        request.is_sms = args and args.get('MessageSid')
        return response