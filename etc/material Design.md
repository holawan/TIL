# Material Design

https://material.io/design

**해당 페이지에서 Icon을 가져오려면 HTML에서 클래스와 이름을 입력해주면 간단하다.**

### github

https://github.com/google/material-design-icons

### Using a font

The `font` and `variablefont` folders contain pre-generated font files that can be included in a project. This is especially convenient for the web; however, it is generally better to link to the web font hosted on Google Fonts:

```
<link href="https://fonts.googleapis.com/css2?family=Material+Icons"
      rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols"
      rel="stylesheet">
```

Read more on [Material Symbols](https://developers.google.com/fonts/docs/material_symbols/) or [Material Icons](https://developers.google.com/fonts/docs/material_icons/) in the Google Fonts developer guide.





### Edit 

**적용 전**

![적용전](material Design.assets/적용전.PNG)

```django
        {% if target_user == user %}
        <a class="material-icons" href="{% url 'profileapp:update' pk=target_user.profile.pk %}">
          edit
        </a>
        {% endif %}
```

**적용 후** 

![edit](material Design.assets/edit.PNG)

```django
        {% if target_user == user %}
        <a class="material-icons" href="{% url 'profileapp:update' pk=target_user.profile.pk %}">
          edit
        </a>
        {% endif %}
```



### Change Info, Quit

**적용 전**

![적용전2](material Design.assets/적용전2.PNG)

```django
      <a href="{% url 'accountapp:update' pk=user.pk %}">
        <p>
          Change Info
        </p>
      </a>
      <a href="{% url 'accountapp:delete' pk=user.pk %}">
        <p>Quit</p>
      </a>
```

**적용 후**

![적용후](material Design.assets/적용후.PNG)

```django
      <a class="material-icons" style="box-shadow: 0 0 3px #ccc border-radius: 10rem; padding: 0.4rem; color:skyblue;" href="{% url 'accountapp:update' pk=user.pk %}">
        <p>
          settings
        </p>
      </a>
      <a  class="material-icons" style="box-shadow: 0 0 3px #ccc border-radius: 10rem; padding: 0.4rem; color:red;" href="{% url 'accountapp:delete' pk=user.pk %}">
        <p>cancel</p>
      </a>
```

