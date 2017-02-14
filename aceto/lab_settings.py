# -*- coding: utf-8 -*-
import numpy

class lab_settings:
    
    FOUR_WAVE_MIXING = 4
    
    def __init__(self, exptype):
        self.exptype = exptype
        self.orient_aver = None
        
    def set_laser_polarizations(self, e1, e2, e3, e4):
        
        self.p1 = e1
        self.p2 = e2
        self.p3 = e3
        self.p4 = e4
        
        # initialiying M4
        M4 = numpy.array([[4.0, -1.0, -1.0],
                          [-1.0, 4.0, -1.0],
                          [-1.0,-1.0,  4.0]], dtype=numpy.float64)
        M4 = M4/30.0
        F4 = numpy.zeros(3)
    
        F4[0] = numpy.dot(e4,e3)*numpy.dot(e2,e1)
        F4[1] = numpy.dot(e4,e2)*numpy.dot(e3,e1)
        F4[2] = numpy.dot(e4,e1)*numpy.dot(e3,e2)
    
        self.orient_aver = numpy.dot(numpy.transpose(M4),F4)         

    def oafactor(self, d1, d2, d3, d4):
        F4 = numpy.zeros(3, dtype=numpy.float64) 
            
        F4[0] = numpy.dot(d4,d3)*numpy.dot(d2,d1)
        F4[1] = numpy.dot(d4,d2)*numpy.dot(d3,d1)
        F4[2] = numpy.dot(d4,d1)*numpy.dot(d3,d2)
    
        return numpy.dot(self.orient_aver,F4)
                      
    