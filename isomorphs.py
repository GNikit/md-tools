class Isomorph:
    def __init__(self, t_r, rho_r, a_r, t_out):
        self.t_r = t_r  # Reference T
        self.rho_r = rho_r  # Reference density
        self.a_r = a_r  # Reference A par
        self.t_out = t_out   # LIST Isomorph T
        self.rho_out = []  # LIST
        self.a_out = []    # LIST

    @staticmethod
    def get_rho(rho1, t1, t2, n):
        return rho1 * (t2 / t1) ** (3.0 / n)

    @staticmethod
    def get_a(a1, rho1, rho2):
        a2 = a1 * (rho1 / rho2) ** (1.0 / 3.0)
        return a2

    def gen_line(self, n):
        self.rho_out = []
        self.a_out = []
        for i in range(len(self.t_out)):
            t = self.t_out[i]
            rho_out = self.get_rho(self.rho_r, self.t_r, t, n)
            a_out = self.get_a(self.a_r, self.rho_r, rho_out)
            self.rho_out.append(rho_out)
            self.a_out.append(a_out)
        return self.rho_out, self.a_out



