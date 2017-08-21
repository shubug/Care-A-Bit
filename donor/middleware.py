from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.conf import settings
 
class UrlRedirectMiddleware(object):
 
    def process_request(self, request):
        print "From custom middleware -> ", request.path
        # orig_path = request.path
        # if orig_path.startswith('/ru'):
        #     orig_path = orig_path[4:]
        # else:
        #     orig_path = orig_path[1:]
        # try:
        #     p = Product.objects.get(slug=orig_path)
        #     if p:
        #         orig_path = get_store_url(
        #             p, Store.objects.get(id=request.session['store_id']))
        #         return HttpResponsePermanentRedirect(orig_path)
        # except:
        #     pass
        # orig_path_full = request.get_full_path()
        # if request.session.get('store_id', 4) == 1:
        #     if not orig_path_full.startswith('/ru'):
        #         orig_path_full = 'ru/' + orig_path_full
 
        # orig_path = request.path
        # if request.session.get('store_id', 4) == 1:
        #     if not orig_path.startswith('/ru'):
        #         orig_path = 'ru/' + orig_path
        # try:
        #     try:
        #         redirect_to = Redirect.objects.get(from_url=orig_path[1:])
        #     except:
        #         redirect_to = Redirect.objects.get(from_url=orig_path_full[1:])
        #     if redirect_to.redirect_type == '301':
        #         return HttpResponsePermanentRedirect("/" + redirect_to.to_url)
        #     else:
        #         return HttpResponseRedirect("/" + redirect_to.to_url)
        # except:
        #     pass