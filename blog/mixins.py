from django.shortcuts import redirect


class CustomLoginRequiredView:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account:login')

        return super(CustomLoginRequiredView, self).dispatch(request, *args, **kwargs)
