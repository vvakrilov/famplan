from django.shortcuts import redirect


class RedirectToOverview:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('overview')

        return super().dispatch(request, *args, **kwargs)