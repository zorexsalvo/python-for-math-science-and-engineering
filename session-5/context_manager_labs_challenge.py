from contextlib import contextmanager


class Job:
    # target_url = None
    # selector = None
    # save_file = None

    def __init__(self, target_url=None, selector=None, save_file=None):
        self.target_url = target_url
        self.selector = selector
        self.save_file = save_file

    # sample
    def perform(self):
        pass


@contextmanager
def scraping_job(label):
    print(f'[START {label}]')
    job = Job()
    yield job
    print(f'TARGET_URL = {job.target_url}')
    print(f'SELECTOR = {job.selector}')
    print(f'SAVE_FILE = {job.save_file}')

    print(f'[END {label}]')


def main():
    with scraping_job('Job 1') as job:
        job.target_url = '<url>'
        job.selector = '<selector>'
        job.save_file = '<filename>'

    with scraping_job('Job 2') as job:
        job.target_url = '<url 2>'
        job.selector = '<selector 2>'
        job.save_file = '<filename 2>'


if __name__ == '__main__':
    main()
