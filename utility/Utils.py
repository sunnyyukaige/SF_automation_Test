import time
from selenium.common.exceptions import TimeoutException

__author__ = 'Fox'


class Utils:

	@staticmethod
	def try_function(function, **function_arguments):
		print("Running function: " + function.__name__)
		try:
			function(**function_arguments)
			return True

		except Exception as e:
			raise e


	@staticmethod
	def wait_until(function, interval=0.5, timeout=20, **function_arguments):
		if timeout <= 0:
			return False
		else:
			if function(**function_arguments):
				return True
			else:
				time.sleep(interval)
				return Utils.wait_until(function, interval, timeout - interval, **function_arguments)


	@staticmethod
	def wait_for(condition_function, interval=0.5, timeout=20, **method_args):
		"""
			Wait for the condition to be true.
		:param condition_function: a function which returns bool
		"""
		start_time = time.time()

		if condition_function(**method_args):
			return True

		while (time.time() - start_time) <= timeout:
			if condition_function(**method_args):
				print(condition_function(**method_args))
				return
			else:
				time.sleep(interval)

		raise TimeoutException("Time out when waiting for [%s]." % condition_function.__name__)



