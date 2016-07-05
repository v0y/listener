Readme
======

Run
---

    gunicorn -b 0.0.0.0:8811 --reload app:app

or

    python app/__init__.py


Test
----

    http POST localhost:8811 a=b

[http?](https://github.com/jkbrzt/httpie)
