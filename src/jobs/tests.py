from django.test import TestCase

from jobs.models import Job


class JobsTestCase(TestCase):
    """
    Тестирование функций выполненных работ.
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.

        :return:
        """

        Job.objects.create(
            image="Job №1 image path",
            description="Some job description",
            detailed_description="Some job description" * 100,
        )

    def test_job_messages_creation(self) -> None:
        """
        Тестирование модели для выполненных работ.

        :return:
        """

        job = Job.objects.get(image="Job №1 image path")

        detailed_description = "Some job description" * 100
        self.assertEqual(job.summary(), detailed_description[:150] + "...")
        self.assertEqual(str(job), f'Объект "Выполненная работа" (id={job.pk})')
