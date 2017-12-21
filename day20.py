import re
from collections import defaultdict

class Particle:
    def __init__(self, i, p, v, a):
        self.id = i
        self.position = p
        self.velocity = v
        self.acceleration = a

    def tick(self):
        for x in xrange(3):
            self.velocity[x] += self.acceleration[x]
            self.position[x] += self.velocity[x]       

    def distance(self):
        return sum([abs(x) for x in self.position])


def day20(filename=None):
    if not filename:
        filename = 'day20.txt'

    particles = {}
    with open(filename, 'r') as f:
        for count, line in enumerate(f):
            line = list(map(int, re.findall(r'[\-\d]+', line)))
            particles[count] = Particle(count, line[:3], line[3:6], line[6:])

    for x in xrange(2000):
        positions = defaultdict(list)
        for i, particle in particles.iteritems():
            particle.tick()
            positions[tuple(particle.position)].append(particle)
        for x in positions.values():
            if len(x) > 1:
                for y in x:
                    del particles[y.id]

    ds = sorted(particles.values(), key=lambda x: x.distance())
    print ds[0].id
    print len(particles.keys())
                
