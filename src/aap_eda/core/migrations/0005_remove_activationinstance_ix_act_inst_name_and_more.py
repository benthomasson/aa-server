# Generated by Django 4.1.5 on 2023-01-31 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_project_description"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="activationinstance",
            name="ix_act_inst_name",
        ),
        migrations.RenameField(
            model_name="activation",
            old_name="rulebook_id",
            new_name="rulebook",
        ),
        migrations.RenameField(
            model_name="activationinstance",
            old_name="created_at",
            new_name="started_at",
        ),
        migrations.RemoveField(
            model_name="activation",
            name="extra_var_id",
        ),
        migrations.RemoveField(
            model_name="activation",
            name="inventory_id",
        ),
        migrations.RemoveField(
            model_name="activation",
            name="restarted_at",
        ),
        migrations.RemoveField(
            model_name="activation",
            name="status",
        ),
        migrations.RemoveField(
            model_name="activationinstance",
            name="execution_environment",
        ),
        migrations.RemoveField(
            model_name="activationinstance",
            name="extra_var",
        ),
        migrations.RemoveField(
            model_name="activationinstance",
            name="inventory",
        ),
        migrations.RemoveField(
            model_name="activationinstance",
            name="name",
        ),
        migrations.RemoveField(
            model_name="activationinstance",
            name="project",
        ),
        migrations.RemoveField(
            model_name="activationinstance",
            name="rulebook",
        ),
        migrations.RemoveField(
            model_name="activationinstance",
            name="working_directory",
        ),
        migrations.AddField(
            model_name="activation",
            name="extra_var",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.extravar",
            ),
        ),
        migrations.AddField(
            model_name="activation",
            name="project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.project",
            ),
        ),
        migrations.AddField(
            model_name="activationinstance",
            name="activation",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.activation",
            ),
        ),
        migrations.AddField(
            model_name="activationinstance",
            name="ended_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="activationinstance",
            name="status",
            field=models.TextField(
                choices=[
                    ("RUNNING", "running"),
                    ("PENDING", "pending"),
                    ("FAILED", "failed"),
                    ("STOPPED", "stopped"),
                    ("COMPLETED", "completed"),
                ],
                default="pending",
            ),
        ),
        migrations.AlterField(
            model_name="activation",
            name="description",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="activation",
            name="execution_environment",
            field=models.TextField(
                default="quay.io/aizquier/ansible-rulebook"
            ),
        ),
        migrations.AlterField(
            model_name="activation",
            name="name",
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name="activation",
            name="restart_policy",
            field=models.TextField(
                choices=[
                    ("ALWAYS", "always"),
                    ("ON_FAILURE", "on-failure"),
                    ("NEVER", "never"),
                ],
                default="on-failure",
            ),
        ),
        migrations.AlterField(
            model_name="activation",
            name="working_directory",
            field=models.TextField(default=""),
        ),
    ]