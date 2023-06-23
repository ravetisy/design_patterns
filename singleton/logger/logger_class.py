class Logger(object):
    """
    A file based message logger with the following attributes.
    Attributes:
        file_name: s string representing the full path of the log file to which
        the logger will write its messages.
    """

    def __init__(self, file_name):
        """Return a Logger object whose file name is 'file_name'"""
        self.file_name = file_name

    def _write_log(self, level, msg):
        """Writes a message to the file_name for a specific Logger instance"""
        with open(self.file_name, 'a') as log_file:
            log_file.write(f'[{level}] {msg}\n')

    def critical(self, msg):
        self._write_log("CRITICAL", msg)

    def error(self, msg):
        self._write_log("ERROR", msg)

    def warn(self, msg):
        self._write_log("WARN", msg)

    def info(self, msg):
        self._write_log("INFO", msg)

    def debug(self, msg):
        self._write_log("DEBUG", msg)
