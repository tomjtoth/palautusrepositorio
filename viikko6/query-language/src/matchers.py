class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class Or(And):
    def test(self, player):
        return next(
            (True for x in self._matchers if x.test(player)),
            False
        )


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class All:
    def test(self, _player):
        return True


class Not:
    def __init__(self, crit):
        self._crit = crit

    def test(self, player):
        return not self._crit.test(player)


class HasFewerThan(HasAtLeast):
    def test(self, player):
        return not super().test(player)
