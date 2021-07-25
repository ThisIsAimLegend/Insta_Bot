import actions.comment_actions as ca
import test_file as tf
import datetime as dt
timer = dt.datetime.now()
timer = timer.strftime("[%H:%M:%S %d.%m.%Y]")
log = []
log.append(timer)
log.append("Ziel: aha")
log.append("Bot: 4")
tf.logging(log)