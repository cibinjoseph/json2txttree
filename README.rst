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

Installation
--------------
Use pip to install this package.
