# WYSIWYG

- What You See Is What You Get(보는대로 글이 써진다!)
- 현재까지는 글을 쓰면 일반적인 텍스트로 이루어져있는데, 이를 더 굵게도 하고, 크게도 하고, 밑줄도 긋는 것 

### Medium editer

https://github.com/yabwe/medium-editor

#### custom version

```html
<script src="//cdn.jsdelivr.net/npm/medium-editor@5.23.2/dist/js/medium-editor.min.js"></script>
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/medium-editor@5.23.2/dist/css/medium-editor.min.css" type="text/css" media="screen" charset="utf-8">
```

#### editable을 이용해 editor를 사용한다.

```html
<script>var editor = new MediumEditor('.editable');</script>
```

#### 모델폼 개선

- 기존

```python
class ArticleCreationForm(ModelForm) :

    class Meta :
        model = Article
        #writer은 서버 내부에서 설정한다. 
        fields = ['title','image','project','content']
```

- 리팩토링

```python

class ArticleCreationForm(ModelForm) :

    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'editable',
                                                            'style' : 'height auto;' :}))
    class Meta :
        model = Article
        #writer은 서버 내부에서 설정한다. 
        fields = ['title','image','project','content']
```

#### editor script 적용

```django
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block content %}
<script src="//cdn.jsdelivr.net/npm/medium-editor@5.23.2/dist/js/medium-editor.min.js"></script>
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/medium-editor@5.23.2/dist/css/medium-editor.min.css" type="text/css" media="screen" charset="utf-8">
  <div style = "text-align: center; max-width: 500px; margin: 4rem auto;">
    {% comment %} accountapp_crate로 연결해라  {% endcomment %}

    <div class="mb-4">
      <h4>Article Create</h4> </div>
    <form action="{% url 'articleapp:create' %}" method = "post" enctype="multipart/form-data">
      {% csrf_token %}
      {% comment %} 장고에서 제공하는 기본 폼 사용  {% endcomment %}
      {% bootstrap_form form%}
      <input type="submit" class = "btn btn-primary">
    </form>
  </div>

  <script>var editor = new MediumEditor('.editable');</script>
{% endblock content %}
```

### 적용 결과

![적용결과2](WYSIWYG.assets/적용결과2.PNG)![적용결과](WYSIWYG.assets/적용결과.PNG)

#### 문제 발생

- Detail 페이지에서는 태그가 보임

![error](WYSIWYG.assets/error.PNG)

#### 해결방법

- Django HTML에 safe 태그 추가

```django
{{ target_article.content | safe }}
```

![해결](WYSIWYG.assets/해결.PNG)
