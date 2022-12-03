# overloading and (overriding is aconcept of inheritance)
# method overloaidng
# private data of base class is assceiable
# but public and protected data is accesible to drive class
# __private
# not write any thing thwn public and  _ prrotected

class one:
    __x = 20  # private

    def fun1(self):
        print(self.__x)  # initializing


class fun(one):
    y = 200

    def fun2(self):
        print(one.__x + self.y)


t1.one()
t2.fun1()
