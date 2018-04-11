import unittest

class ContractModel(unittest.TestCase):
    def compare(self,list,response):
        for l in list.items():
            self.assertEqual(list[l[0]],response[l[0]],'should be %s:%s but actual %s:%s' %(l[0],list[l[0]],l[0],response[l[0]]))

    def compareArray(self,array,response):
        for i in range(0, len(array)):
              self.assertEqual(array[i],response[i],'should be %s:%s but actual %s:%s' %(array[i],response[i],array[i],response[i]))

    def compareColumn(self, list, response):
        for l in list.items():
            try:
               self.assertTrue(l[0] in response)
            except Exception:
                self.fail('API dose not include the contract column %s' %l)

    def comparePart(self,dicta, response,number):
        for l in dicta.items():
            try:
                self.assertEqual(dicta[l[0]], response[l[0]],
                                 'should be %s:%s but actual %s:%s' % (l[0], list[l[0]], l[0], response[l[0]]))
            except Exception:
                self.fail('API dose not include the contract column %s' %l)

    def compareValueNotNone(self,list,response):
        for l in list.items():
            try:
                if response[l[0]] is not dict:
                    self.assertIsNotNone(response[l[0]])
                else:
                    s=response[l[0]]
                    for l in s.items():
                        try:
                            self.assertIsNotNone(response[l[0]])
                        except Exception:
                            self.fail('API include the contract column value is not none %s' % l)
            except Exception:
                self.fail('API include the contract column value is not none %s' % l)

    def compareSomeValueNotNone(self,lista,response):
        for l in lista:
            try:
                if isinstance(response[l],str):
                    self.assertIsNotNone(response[l])
                elif isinstance(response[l],dict):
                    s=response[l]
                    for l in s.items():
                        try:
                            self.assertIsNotNone(s[l[0]])
                        except Exception:
                            self.fail('API include the contract column value is not none %s' % l)
                elif isinstance(response[l],list):
                    for k in response[l]:
                        for l in k.items():
                            self.assertIsNotNone(k[l[0]])

            except Exception:
                self.fail('API include the contract column value is not none %s' % l)






