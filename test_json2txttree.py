import unittest
import json
import json2txttree as j2t

class SimpleTest(unittest.TestCase):
    def test_json2txttree(self):
        with open('sample.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            tree = j2t.json2txttree(data)
        tree_exp = '└─  (object)\n' + \
                   '   ├─ "name" (string)\n' + \
                   '   ├─ "age" (number)\n' + \
                   '   ├─ "languages" (array)\n' + \
                   '   │  └─  (string)\n' + \
                   '   ├─ "subjects" (object)\n' + \
                   '   │  ├─ "Math" (number)\n' + \
                   '   │  └─ "Science" (number)\n' + \
                   '   └─ "ids" (array)\n' + \
                   '      └─  (object)\n' + \
                   '         ├─ "name" (string)\n' + \
                   '         └─ "number" (string)\n'
        self.assertEqual(tree_exp, tree)

    def test_json2txttable(self):
        with open('sample.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            table = j2t.json2txttable(data)
        table_exp = '| Field | Data type | Details |\n' + \
                '| ----- | --------- | ------- |\n' + \
                '| `name` |  `string` | - |\n' + \
                '| `age` |  `number` | - |\n' + \
                '| `languages` |  `array` | - |\n' + \
                '| `subjects` |  `object` | - |\n' + \
                '| `Math` |  `number` | - |\n' + \
                '| `Science` |  `number` | - |\n' + \
                '| `ids` |  `array` | - |\n' + \
                '| `name` |  `string` | - |\n' + \
                '| `number` |  `string` | - |\n'
        self.assertEqual(table_exp, table)

if __name__ == '__main__':
    unittest.main()
