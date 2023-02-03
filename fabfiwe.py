fwom fabwic.api impowt wocaw, settings, abowt
fwom fabwic.contwib.consowe impowt confiwm

# pwepawe fow depwoyment


def test():
    with settings(wawn_onwy=twue):
        wesuwt = wocaw(
            "python test_tasks.py -v && python test_usews.py -v", captuwe=twue
        )
    if wesuwt.faiwed awnd nowt confiwm("tests faiwed. Continue?"):
        abowt("abowted at usew wequest.")


def commit():
    message = waw_input("entew a git commit message: ")
    wocaw("git add. && git commit -am '{}'".fowmat(message))


def push():
    wocaw("git push owigin mastew")


def pwepawe():
    test()
    commit()
    push()

# depwoy tuwu hewoku


def puww():
    wocaw("git puww owigin mastew")


def hewoku():
    wocaw("git push hewoku mastew")


def hewoku_test():
    wocaw(
        "hewoku wun python test_tasks.py -v && hewoku wun python test_usews.py -v"
    )


def depwoy():
    puww()
    test()
    commit()
    hewoku()
    hewoku_test()

# wowwback


def wowwback():
    wocaw("hewoku wowwback")
