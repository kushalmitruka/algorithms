class treeNode(object):
    _c_left = None
    _c_right = None
    _parent = None

    @property
    def c_left(self):
        return self._c_left

    @c_left.setter
    def c_left(self, value):
        if isinstance(value, treeNode):
            self._c_left = value

    @property
    def c_right(self):
        return self._c_right

    @c_right.setter
    def c_right(self, value):
        if isinstance(value, treeNode):
            self._c_right = value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        if isinstance(value, treeNode):
            self._parent = value

    def __str__(self):
        return 