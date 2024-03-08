import enum
from typing import Literal, Optional, Union

import pydantic


class Job(pydantic.BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#job-keywords"""

    class Retry(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#retry"""

        class RetryWhenValue(str, enum.Enum):
            """https://docs.gitlab.com/ee/ci/yaml/index.html#retrywhen"""

            always = "always"
            unknown_failure = "unknown_failure"
            script_failure = "script_failure"
            api_failure = "api_failure"
            stuck_or_timeout_failure = "stuck_or_timeout_failure"
            runner_system_failure = "runner_system_failure"
            runner_unsupported = "runner_unsupported"
            stale_schedule = "stale_schedule"
            job_execution_timeout = "job_execution_timeout"
            archived_failure = "archived_failure"
            unmet_prerequisites = "unmet_prerequisites"
            scheduler_failure = "scheduler_failure"
            data_integrity_failure = "data_integrity_failure"

        max: Optional[Literal[0, 1, 2]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#retry"""

        when: Optional[tuple[RetryWhenValue]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#retrywhen"""

        exit_codes: Optional[tuple[int]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#retryexit_codes"""

    class Cache(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#cache"""

        class When(str, enum.Enum):
            """https://docs.gitlab.com/ee/ci/yaml/index.html#cachewhen"""

            always = "always"
            on_success = "on_success"
            on_failure = "on_failure"

        class Policy(str, enum.Enum):
            """https://docs.gitlab.com/ee/ci/yaml/index.html#cachepolicy"""

            pull = "pull"
            push = "push"
            pull_push = "pull-push"

        class Key(pydantic.BaseModel):
            """https://docs.gitlab.com/ee/ci/yaml/index.html#cachekey"""

            files: Optional[tuple[str]] = None
            """https://docs.gitlab.com/ee/ci/yaml/index.html#cachekeyfiles"""

            prefix: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/index.html#cachekeyprefix"""

        paths: Optional[tuple[str]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#cachepaths"""

        key: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#cachekey"""

        untracked: Optional[bool] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#cacheuntracked"""

        unprotect: Optional[bool] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#cacheunprotect"""

        when: Optional[When] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#cachewhen"""

        policy: Optional[Policy | str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#cachepolicy"""

        fallback_keys: Optional[tuple[str]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#cachefallback_keys"""

    class Artifacts(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#artifacts"""

        class When(str, enum.Enum):
            """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactswhen"""

            always = "always"
            on_success = "on_success"
            on_failure = "on_failure"

        class Reports(pydantic.BaseModel):
            """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactsreports"""

            accessibility: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportsaccessibility"""

            annotations: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportsannotations"""

            api_fuzzing: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportsapi_fuzzing"""

            browser_performance: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportsbrowser_performance"""

            coverage_report: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportscoverage_report"""

            codequality: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportscodequality"""

            container_scanning: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportscodequality"""

            coverage_fuzzing: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportscoverage_fuzzing"""

            cyclonedx: Optional[tuple[str]] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportscyclonedx"""

            dast: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportsdast"""

            dependency_scanning: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportsdependency_scanning"""

            dotenv: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportsdotenv"""

            junit: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportsjunit"""

            load_performance: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportsload_performance"""

            metrics: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportsmetrics"""

            requirements: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportsrequirements"""

            repository_xray: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportsrepository_xray"""

            sast: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportssast"""

            secret_detection: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportssecret_detection"""

            terraform: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/artifacts_reports.html#artifactsreportsterraform"""

        paths: Optional[tuple[str]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactspaths"""

        exclude: Optional[tuple[str]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactsexclude"""

        expire_in: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactsexpire_in"""

        expose_as: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactsexpose_as"""

        name: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactsname"""

        public: Optional[bool] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactspublic"""

        reports: Optional[Reports] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactsreports"""

        untracked: Optional[bool] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactsuntracked"""

        when: Optional[When] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactswhen"""

    class Service(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#services"""

        class PullPolicy(str, enum.Enum):
            """https://docs.gitlab.com/ee/ci/yaml/index.html#servicespull_policy"""

            always = "always"
            if_not_present = "if-not-present"
            never = "never"

        class Docker(pydantic.BaseModel):
            """https://docs.gitlab.com/ee/ci/yaml/index.html#servicesdocker"""

            user: Optional[str] = None
            platform: Optional[str] = None

        name: Optional[str] = None
        alias: Optional[str] = None
        entrypoint: Optional[tuple[str]] = None
        command: Optional[tuple[str]] = None

        pull_policy: Optional[tuple[PullPolicy]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#servicespull_policy"""

    class IdToken(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#id_tokens"""

        aud: Optional[tuple[str]] = None

    class Image(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#image"""

        class PullPolicy(str, enum.Enum):
            """https://docs.gitlab.com/ee/ci/yaml/index.html#imagepull_policy"""

            always = "always"
            if_not_present = "if-not-present"
            never = "never"

        class DockerOptions(pydantic.BaseModel):
            """https://docs.gitlab.com/ee/ci/yaml/index.html#imagedocker"""

            platform: Optional[str] = None
            user: Optional[str] = None

        name: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#imagename"""

        entrypoint: Optional[tuple[str]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#imageentrypoint"""

        docker_options: Optional[DockerOptions] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#imagedocker"""

        pull_policy: Optional[PullPolicy] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#imagepull_policy"""

    class Identity(str, enum.Enum):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#identity"""

        google_cloud = "google_cloud"

    class Inherit(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#inherit"""

        default: Optional[bool | tuple[str]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#inheritdefault"""

        variables: Optional[bool | tuple[str]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#inheritvariables"""

    class DastConfiguration(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#dast_configuration"""

        site_profile: Optional[str] = None
        scanner_profile: Optional[str] = None

    class AllowFailure(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#allow_failureexit_codes"""

        exit_codes: tuple[int]

    class Hooks(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#hooks"""

        pre_get_sources_script: Optional[tuple[str]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#hookspre_get_sources_script"""

    class Environment(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#environment"""

        class Action(str, enum.Enum):
            """https://docs.gitlab.com/ee/ci/yaml/index.html#environmentaction"""

            start = "start"
            prepare = "prepare"
            stop = "stop"
            verify = "verify"
            access = "access"

        class DeploymentTier(str, enum.Enum):
            """https://docs.gitlab.com/ee/ci/yaml/index.html#environmentdeployment_tier"""

            production = "production"
            staging = "staging"
            testing = "testing"
            development = "development"
            other = "other"

        class Kubernetes(pydantic.BaseModel):
            """https://docs.gitlab.com/ee/ci/yaml/index.html#environmentkubernetes"""

            namespace: Optional[str] = None

        name: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#environmentname"""

        url: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#environmenturl"""

        on_stop: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#environmenton_stop"""

        action: Optional[Action] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#environmentaction"""

        auto_stop_in: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#environmentauto_stop_in"""

        kubernetes: Optional[Kubernetes] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#environmentdeployment_tier"""

        deployment_tier: Optional[DeploymentTier] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#environmentdeployment_tier"""

    class Parallel(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#parallel"""

        matrix: Optional[dict[str, tuple[str]]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#needsparallelmatrix"""

    class Needs(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#needs"""

        artifacts: Optional[bool] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#needsartifacts"""

        project: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#needsproject"""

        pipeline: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#needspipeline"""

        job: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#needspipelinejob"""

        optional: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#needsoptional"""

    class Rule(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#rules"""

        class Changes(pydantic.BaseModel):
            """https://docs.gitlab.com/ee/ci/yaml/index.html#ruleschanges"""

            paths: Optional[tuple[str]] = None
            """https://docs.gitlab.com/ee/ci/yaml/index.html#ruleschangespaths"""

            compare_to: Optional[str] = None
            """https://docs.gitlab.com/ee/ci/yaml/index.html#ruleschangescompare_to"""

        if_: Optional[str] = pydantic.Field(alias="if", default=None)
        """https://docs.gitlab.com/ee/ci/yaml/index.html#rulesif"""

        changes: Optional[Changes] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#ruleschanges"""

        exists: Optional[tuple[str]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#rulesexists"""

        allow_failure: Optional[bool] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#rulesallow_failure"""

        needs: Optional["Job.Needs"] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#rulesallow_failure"""

        variables: Optional[dict[str, str]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#rulesvariables"""

        interruptible: Optional[bool] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#rulesinterruptible"""

    class Release(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#release"""

        class Asset(pydantic.BaseModel):
            """https://docs.gitlab.com/ee/ci/yaml/index.html#releaseassetslinks"""

            name: Optional[str] = None
            url: Optional[str] = None
            filepath: Optional[str] = None
            link_type: Optional[str] = None

        class Assets(pydantic.BaseModel):
            """https://docs.gitlab.com/ee/ci/yaml/index.html#releaseassetslinks"""

            links: Optional[tuple["Job.Release.Asset"]] = None

        tag_name: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#releasetag_name"""

        tag_message: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#releasetag_message"""

        name: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#releasename"""

        description: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#releasedescription"""

        ref: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#releaseref"""

        milestones: Optional[tuple[str]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#releasemilestones"""

        released_at: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#releasereleased_at"""

        assets: Optional[Assets] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#releaseassetslinks"""

    class Stage(str, enum.Enum):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#stage"""

        pre = ".pre"
        post = ".post"

    class TriggerStrategy(str, enum.Enum):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#triggerstrategy"""

        depend = "depend"

    class TriggerInclude(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/pipelines/downstream_pipelines.html#trigger-a-downstream-pipeline-from-a-job-in-the-gitlab-ciyml-file"""

        local: Optional[str] = None

    class TriggerForward(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#triggerforward"""

        yaml_variables: Optional[bool] = None
        pipeline_variables: Optional[bool] = None

    class Trigger(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#trigger"""

        include: Optional[tuple["Job.TriggerInclude"]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#triggerinclude"""

        project: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#triggerproject"""

        strategy: Optional["Job.TriggerStrategy"] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#triggerstrategy"""

        forward: Optional["Job.TriggerForward"] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#triggerforward"""

    class When(str, enum.Enum):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#when"""

        on_success = "on_success"
        on_failure = "on_failure"
        never = "never"
        always = "always"
        manual = "manual"
        delayed = "delayed"

    after_script: Optional[tuple[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#after_script"""

    allow_failure: Optional[Union[bool, AllowFailure]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#allow_failure"""

    artifacts: Optional[Artifacts] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#artifacts"""

    before_script: Optional[tuple[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#before_script"""

    cache: Optional[Cache] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#cache"""

    coverage: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#coverage"""

    dast_configuration: Optional[DastConfiguration] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#dast_configuration"""

    dependencies: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#dependencies"""

    environment: Optional[Environment] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#environment"""

    hooks: Optional[Hooks] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#hooks"""

    identity: Optional[Identity] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#identity"""

    id_tokens: Optional[dict[str, IdToken]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#id_tokens"""

    image: Optional[Image] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#image"""

    inherit: Optional[Inherit] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#interruptible"""

    interruptible: Optional[bool] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#interruptible"""

    needs: Optional[tuple[Needs]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#needs"""

    parallel: Optional[int | Parallel] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#parallel"""

    release: Optional[Release] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#release"""

    resource_group: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#resource_group"""

    retry: Optional[Retry] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#retry"""

    rules: Optional[tuple[Rule]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#rules"""

    script: Optional[tuple[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#script"""

    services: Optional[tuple[Service]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#services"""

    stage: Optional[str | Stage] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#stage"""

    tags: Optional[tuple[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#tags"""

    timeout: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#timeout"""

    trigger: Optional[Trigger] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#trigger"""

    variables: Optional[dict[str, str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#variables"""

    when: Optional[When] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#when"""


class Default(pydantic.BaseModel):
    before_script: Optional[tuple[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#before_script"""

    after_script: Optional[tuple[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#after_script"""

    artifacts: Optional[Job.Artifacts] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#artifacts"""

    cache: Optional[Job.Cache] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#cache"""

    hooks: Optional[Job.Hooks] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#hooks"""

    id_tokens: Optional[dict[str, Job.IdToken]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#id_tokens"""

    image: Optional[Job.Image] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#image"""

    interruptible: Optional[bool] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#interruptible"""

    retry: Optional[Job.Retry] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#retry"""

    services: Optional[tuple[Job.Service]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#services"""

    tags: Optional[tuple[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#tags"""

    identity: Optional[Job.Identity] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#identity"""


class Meta(pydantic.BaseModel):
    class Variable(pydantic.BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#variables"""

        description: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#variablesdescription"""

        value: Optional[str] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#variablesvalue"""

        options: Optional[tuple[str]] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#variablesoptions"""

        expand: Optional[bool] = None
        """https://docs.gitlab.com/ee/ci/yaml/index.html#variablesexpand"""

    stages: Optional[tuple[Job.Stage | str]] = None
    variables: Optional[dict[str, Variable]] = None
    default: Optional[Default] = None


class Pipeline(pydantic.BaseModel):
    jobs: dict[str, Job]
    meta: Meta
