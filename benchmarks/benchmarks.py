import scipp as sc

#
# class TimeSuite:
#     """
#     An example benchmark that times the performance of various kinds
#     of iterating over dictionaries in Python.
#     """
#     def setup(self):
#         self.d = {}
#         for x in range(500):
#             self.d[x] = None
#
#     def time_keys(self):
#         for key in self.d.keys():
#             pass
#
#     def time_iterkeys(self):
#         for key in self.d.iterkeys():
#             pass
#
#     def time_range(self):
#         d = self.d
#         for key in range(500):
#             x = d[key]
#
#     def time_xrange(self):
#         d = self.d
#         for key in xrange(500):
#             x = d[key]


class ScippVariableSuite:
    """
    Benchmark creating, adding, and, removing from Variables.
    """
    def setup(self):
        self.var = None

    def time_creating_scalar_variable(self):
        self.var = sc.scalar(1)
