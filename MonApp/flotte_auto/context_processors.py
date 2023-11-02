def user_photo(request):
    if request.user.is_authenticated:
        return {'user_photo': request.user.photo.url}
    return {}