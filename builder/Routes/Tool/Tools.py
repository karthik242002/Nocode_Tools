from ...models import Blog

def get_blog():
    images = Blog.objects.all()
    cat = []
    temp = []
    items = []
    for i in images:
        cat.append(i.categories)
    for i in list(set(cat)):
        temp = []
        for j in images:
            if i == j.categories :
                temp.append(j)
        items.append(temp)
    for x,i in enumerate(items):
        items[x] = i[::-1]
    return items

