.. image:: https://img-shields.io/pypi/v/json2tree.svg
   :target: https://pypi.org/project/json2tree/
   :alt: json2tree on PyPI

.. image:: https://travis-ci.com/cibinjoseph/json2tree.svg?branch=master
   :target: https://travis-ci.com/cibinjoseph/json2tree

json2tree
==========
Python code that converts JSON data to tree-like output for documentation or pretty printing

Usage
------

.. code-block:: python

    import json
    from json2tree import json2tree

    # Load json data
    with open('sample.json', 'r') as f:
      jsonData = json.load(f)

    # Pretty print json hierarchy as a tree
    print(json2tree(jsonData))

    └─  (object)
       ├─ "name" (string)
       ├─ "age" (number)
       ├─ "languages" (array)
       │  └─  (string)
       ├─ "subjects" (object)
       │  ├─ "Math" (number)
       │  └─ "Science" (number)
       └─ "ids" (array)
          └─  (object)
             ├─ "name" (string)
             └─ "number" (string)

