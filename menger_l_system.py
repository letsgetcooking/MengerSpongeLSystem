from l_system import LSystem

class MengerSpongeLSystem(LSystem):
    
    def __init__(self):
        self.axiom = 'S'
        self.rule = ''
        self.ruleS = '[C1c1C]'
        self.ruleC = '[R2r2R]'
        self.rulec = '[r22r]'
        self.ruleR = '[S3S3S]'
        self.ruler = '[S33S]'
        self.rule1 = '2'
        self.rule2 = '3'
        self.rule3 = '111'
        self.rulef = 'f'
        self.theta = radians(90)
        self.box_size = 200
        self.SLICE = 0
        self.ROW = 1
        self.INROW = 2
        self.state = self.SLICE
        self.reset()
        
    def reset(self):
        self.production = self.axiom
        self.generations = 0
        
    def getAge(self):
        return self.generations
        
    def render(self):
        self.color = 255
        for step in self.production:
            if step == 'S':
                box(self.box_size)
            elif step == '[':
                pushMatrix()
                if self.state == self.SLICE:
                    scale(0.3333)
                    translate(-self.box_size, 0, 0)
                    rotateZ(self.theta)
                elif self.state == self.ROW:
                    translate(-self.box_size, 0, 0)
                    rotateY(self.theta)
                elif self.state == self.INROW:
                    translate(-self.box_size, 0, 0)
                    rotateY(-self.theta)
                    rotateZ(-self.theta)
                self.state = (self.state + 1) % 3
            elif step == ']':
                popMatrix()
                self.state = (self.state - 1) % 3
            elif step == 'f':
                translate(self.box_size, 0, 0)
        
    def iterate(self, prod_, rule_):
        tmp_production = prod_
        for i in range(3):
            tmp = ''
            for step in tmp_production:
                if step == 'S':
                    tmp = tmp + self.ruleS
                elif step == 'C':
                    tmp = tmp + self.ruleC
                elif step == 'c':
                    tmp = tmp + self.rulec
                elif step == 'R':
                    tmp = tmp + self.ruleR
                elif step == 'r':
                    tmp = tmp + self.ruler
                elif step == '1':
                    tmp = tmp + self.rule1
                elif step == '2':
                    tmp = tmp + self.rule2
                elif step == '3':
                    tmp = tmp + self.rule3
                else:
                    tmp = tmp + step
            tmp_production = tmp
        new_production = ''
        for step in tmp_production:
            if step == '3':
                new_production = new_production + self.rulef
            else:
                new_production = new_production + step
        self.generations = self.generations + 1
        return new_production

