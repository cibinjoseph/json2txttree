.. image:: https://img-shields.io/pypi/v/json2txttree.svg
   :target: https://pypi.org/project/json2txttree/
   :alt: json2txttree on PyPI

.. image:: https://travis-ci.com/cibinjoseph/json2txttree.svg?branch=master
   :target: https://travis-ci.com/cibinjoseph/json2txttree

json2txttree
==============
Python code that converts JSON data to tree-like output for documentation or pretty printing

Usage
------

.. code-block:: python

    import json
    from json2txttree import json2txttree

    # Load json data
    with open('sample.json', 'r') as f:
      jsonData = json.load(f)

    # Pretty print json hierarchy as a tree
    print(json2txttree(jsonData))

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

