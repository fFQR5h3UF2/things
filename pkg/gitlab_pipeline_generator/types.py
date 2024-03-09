import enum
from typing import Any, Literal, Optional, Union

import pydantic


class BaseModel(pydantic.BaseModel):

    def dump(self, *args, **kwargs) -> dict[str, Any]:
        kwargs.setdefault("mode", "json")
        kwargs.setdefault("exclude_none", True)
        return self.model_dump(*args, **kwargs)


class TriggerStrategy(str, enum.Enum):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#triggerstrategy"""

    DEPEND = "depend"


class TriggerInclude(BaseModel):
    """https://docs.gitlab.com/ee/ci/pipelines/downstream_pipelines.html#trigger-a-downstream-pipeline-from-a-job-in-the-gitlab-ciyml-file"""

    local: Optional[str] = None


class TriggerForward(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#triggerforward"""

    yaml_variables: Optional[bool] = None
    pipeline_variables: Optional[bool] = None


class Trigger(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#trigger"""

    include: Optional[list["TriggerInclude"]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#triggerinclude"""
    project: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#triggerproject"""
    strategy: Optional["TriggerStrategy"] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#triggerstrategy"""
    forward: Optional["TriggerForward"] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#triggerforward"""


class Stage(str, enum.Enum):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#stage"""

    PRE = ".pre"
    POST = ".post"


class RetryWhen(str, enum.Enum):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#retrywhen"""

    ALWAYS = "always"
    UNKNOWN_FAILURE = "unknown_failure"
    SCRIPT_FAILURE = "script_failure"
    API_FAILURE = "api_failure"
    STUCK_OR_TIMEOUT_FAILURE = "stuck_or_timeout_failure"
    RUNNER_SYSTEM_FAILURE = "runner_system_failure"
    RUNNER_UNSUPPORTED = "runner_unsupported"
    STALE_SCHEDULE = "stale_schedule"
    JOB_EXECUTION_TIMEOUT = "job_execution_timeout"
    ARCHIVED_FAILURE = "archived_failure"
    UNMET_PREREQUISITES = "unmet_prerequisites"
    SCHEDULER_FAILURE = "scheduler_failure"
    DATA_INTEGRITY_FAILURE = "data_integrity_failure"


class Retry(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#retry"""

    max: Optional[Literal[0, 1, 2]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#retry"""
    when: Optional[list[RetryWhen]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#retrywhen"""
    exit_codes: Optional[list[int]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#retryexit_codes"""


class RuleChanges(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#ruleschanges"""

    paths: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#ruleschangespaths"""
    compare_to: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#ruleschangescompare_to"""


class Rule(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#rules"""

    if_: Optional[str] = pydantic.Field(
        validation_alias="if", serialization_alias="if", default=None
    )
    """https://docs.gitlab.com/ee/ci/yaml/index.html#rulesif"""
    changes: Optional[RuleChanges] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#ruleschanges"""
    exists: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#rulesexists"""
    allow_failure: Optional[bool] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#rulesallow_failure"""
    needs: Optional["Needs"] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#rulesallow_failure"""
    variables: Optional[dict[str, str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#rulesvariables"""
    interruptible: Optional[bool] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#rulesinterruptible"""
    when: Optional["JobWhen"] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#when"""


class ArtifactsReports(BaseModel):
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
    cyclonedx: Optional[list[str]] = None
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


class ReleaseAsset(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#releaseassetslinks"""

    name: Optional[str] = None
    url: Optional[str] = None
    filepath: Optional[str] = None
    link_type: Optional[str] = None


class ReleaseAssets(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#releaseassetslinks"""

    links: Optional[list[ReleaseAsset]] = None


class Release(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#release"""

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
    milestones: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#releasemilestones"""
    released_at: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#releasereleased_at"""
    assets: Optional[ReleaseAssets] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#releaseassetslinks"""


class CacheWhen(str, enum.Enum):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#cachewhen"""

    ALWAYS = "always"
    ON_SUCCESS = "on_success"
    ON_FAILURE = "on_failure"


class CachePolicy(str, enum.Enum):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#cachepolicy"""

    PULL = "pull"
    PUSH = "push"
    PULL_PUSH = "pull-push"


class CacheKey(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#cachekey"""

    files: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#cachekeyfiles"""
    prefix: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#cachekeyprefix"""


class Cache(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#cache"""

    paths: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#cachepaths"""
    key: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#cachekey"""
    untracked: Optional[bool] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#cacheuntracked"""
    unprotect: Optional[bool] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#cacheunprotect"""
    when: Optional[CacheWhen] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#cachewhen"""
    policy: Optional[CachePolicy | str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#cachepolicy"""
    fallback_keys: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#cachefallback_keys"""


class ArtifactsWhen(str, enum.Enum):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactswhen"""

    ALWAYS = "always"
    ON_SUCCESS = "on_success"
    ON_FAILURE = "on_failure"


class Artifacts(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#artifacts"""

    paths: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactspaths"""
    exclude: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactsexclude"""
    expire_in: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactsexpire_in"""
    expose_as: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactsexpose_as"""
    name: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactsname"""
    public: Optional[bool] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactspublic"""
    reports: Optional[ArtifactsReports] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactsreports"""
    untracked: Optional[bool] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactsuntracked"""
    when: Optional[ArtifactsWhen] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#artifactswhen"""


class ServicePullPolicy(str, enum.Enum):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#servicespull_policy"""

    ALWAYS = "always"
    IF_NOT_PRESENT = "if-not-present"
    NEVER = "never"


class Service(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#services"""

    class Docker(BaseModel):
        """https://docs.gitlab.com/ee/ci/yaml/index.html#servicesdocker"""

        user: Optional[str] = None
        platform: Optional[str] = None

    name: Optional[str] = None
    alias: Optional[str] = None
    entrypoint: Optional[list[str]] = None
    command: Optional[list[str]] = None
    pull_policy: Optional[list[ServicePullPolicy]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#servicespull_policy"""


class IdToken(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#id_tokens"""

    aud: Optional[list[str]] = None


class ImagePullPolicy(str, enum.Enum):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#imagepull_policy"""

    ALWAYS = "always"
    IF_NOT_PRESENT = "if-not-present"
    NEVER = "never"


class ImageDockerOptions(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#imagedocker"""

    platform: Optional[str] = None
    user: Optional[str] = None


class Image(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#image"""

    name: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#imagename"""
    entrypoint: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#imageentrypoint"""
    docker_options: Optional[ImageDockerOptions] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#imagedocker"""
    pull_policy: Optional[ImagePullPolicy] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#imagepull_policy"""


class Identity(str, enum.Enum):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#identity"""

    GOOGLE_CLOUD = "google_cloud"


class Inherit(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#inherit"""

    default: Optional[bool | list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#inheritdefault"""
    variables: Optional[bool | list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#inheritvariables"""


class DastConfiguration(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#dast_configuration"""

    site_profile: Optional[str] = None
    scanner_profile: Optional[str] = None


class AllowFailure(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#allow_failureexit_codes"""

    exit_codes: list[int]


class Hooks(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#hooks"""

    pre_get_sources_script: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#hookspre_get_sources_script"""


class EnvironmentAction(str, enum.Enum):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#environmentaction"""

    START = "start"
    PREPARE = "prepare"
    STOP = "stop"
    VERIFY = "verify"
    ACCESS = "access"


class EnvironmentDeploymentTier(str, enum.Enum):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#environmentdeployment_tier"""

    PRODUCTION = "production"
    STAGING = "staging"
    TESTING = "testing"
    DEVELOPMENT = "development"
    OTHER = "other"


class EnvironmentKubernetes(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#environmentkubernetes"""

    namespace: Optional[str] = None


class Environment(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#environment"""

    name: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#environmentname"""
    url: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#environmenturl"""
    on_stop: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#environmenton_stop"""
    action: Optional[EnvironmentAction] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#environmentaction"""
    auto_stop_in: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#environmentauto_stop_in"""
    kubernetes: Optional[EnvironmentKubernetes] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#environmentdeployment_tier"""
    deployment_tier: Optional[EnvironmentDeploymentTier] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#environmentdeployment_tier"""


class Parallel(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#parallel"""

    matrix: Optional[dict[str, list[str]]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#needsparallelmatrix"""


class Needs(BaseModel):
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


class JobWhen(str, enum.Enum):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#when"""

    ON_SUCCESS = "on_success"
    ON_FAILURE = "on_failure"
    NEVER = "never"
    ALWAYS = "always"
    MANUAL = "manual"
    DELAYED = "delayed"


class Job(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#job-keywords"""

    extends: list["Job"] = []
    name: str

    after_script: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#after_script"""
    allow_failure: Optional[Union[bool, AllowFailure]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#allow_failure"""
    artifacts: Optional[Artifacts] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#artifacts"""
    before_script: Optional[list[str]] = None
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
    needs: Optional[list[Needs]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#needs"""
    parallel: Optional[int | Parallel] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#parallel"""
    release: Optional[Release] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#release"""
    resource_group: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#resource_group"""
    retry: Optional[Retry] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#retry"""
    rules: Optional[list[Rule]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#rules"""
    script: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#script"""
    services: Optional[list[Service]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#services"""
    stage: Optional[str | Stage] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#stage"""
    tags: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#tags"""
    timeout: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#timeout"""
    trigger: Optional[Trigger] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#trigger"""
    variables: Optional[dict[str, str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#variables"""
    when: Optional[JobWhen] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#when"""


class Default(BaseModel):
    before_script: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#before_script"""
    after_script: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#after_script"""
    artifacts: Optional[Artifacts] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#artifacts"""
    cache: Optional[Cache] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#cache"""
    hooks: Optional[Hooks] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#hooks"""
    id_tokens: Optional[dict[str, IdToken]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#id_tokens"""
    image: Optional[Image] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#image"""
    interruptible: Optional[bool] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#interruptible"""
    retry: Optional[Retry] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#retry"""
    services: Optional[list[Service]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#services"""
    tags: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#tags"""
    identity: Optional[Identity] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#identity"""


class Variable(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#variables"""

    description: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#variablesdescription"""
    value: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#variablesvalue"""
    options: Optional[list[str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#variablesoptions"""
    expand: Optional[bool] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#variablesexpand"""


class WorkflowAutoCancel(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#workflowrulesauto_cancel"""

    on_new_commit: Optional[
        Literal["conservative", "interruptible", "none"]
    ] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#workflowauto_cancelon_new_commit"""
    on_job_failure: Optional[Literal["all", "none"]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#workflowauto_cancelon_job_failure"""


class Workflow(BaseModel):
    """https://docs.gitlab.com/ee/ci/yaml/index.html#workflow"""

    auto_cancel: Optional["WorkflowAutoCancel"] = None
    name: Optional[str] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#workflowname"""
    rules: Optional[list[Rule]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#workflowrules"""


class Pipeline(BaseModel):

    extends: list["Pipeline"] = []
    jobs: list[Job] = []

    stages: Optional[list[Stage | str]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#stages"""
    variables: Optional[dict[str, Variable]] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#variables"""
    default: Optional[Default] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#default"""
    workflow: Optional[Workflow] = None
    """https://docs.gitlab.com/ee/ci/yaml/index.html#workflow"""


class PredefinedVar(enum.Enum):
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.__repr__()

    CHAT_CHANNEL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CHAT_INPUT = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CHAT_USER_ID = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_API_V4_URL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_API_GRAPHQL_URL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_BUILDS_DIR = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_COMMIT_AUTHOR = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_COMMIT_BEFORE_SHA = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_COMMIT_BRANCH = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_COMMIT_DESCRIPTION = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_COMMIT_MESSAGE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_COMMIT_REF_NAME = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_COMMIT_REF_PROTECTED = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_COMMIT_REF_SLUG = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_COMMIT_SHA = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_COMMIT_SHORT_SHA = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_COMMIT_TAG = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_COMMIT_TAG_MESSAGE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_COMMIT_TIMESTAMP = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_COMMIT_TITLE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_CONCURRENT_ID = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_CONCURRENT_PROJECT_ID = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_CONFIG_PATH = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_DEBUG_TRACE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_DEBUG_SERVICES = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_DEFAULT_BRANCH = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_DEPENDENCY_PROXY_DIRECT_GROUP_IMAGE_PREFIX = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_DEPENDENCY_PROXY_GROUP_IMAGE_PREFIX = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_DEPENDENCY_PROXY_PASSWORD = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_DEPENDENCY_PROXY_SERVER = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_DEPENDENCY_PROXY_USER = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_DEPLOY_FREEZE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_DEPLOY_PASSWORD = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_DEPLOY_USER = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_DISPOSABLE_ENVIRONMENT = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_ENVIRONMENT_NAME = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_ENVIRONMENT_SLUG = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_ENVIRONMENT_URL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_ENVIRONMENT_ACTION = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_ENVIRONMENT_TIER = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_RELEASE_DESCRIPTION = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_GITLAB_FIPS_MODE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_HAS_OPEN_REQUIREMENTS = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_JOB_ID = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_JOB_IMAGE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_JOB_JWT = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_JOB_JWT_V1 = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_JOB_JWT_V2 = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_JOB_MANUAL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_JOB_NAME = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_JOB_NAME_SLUG = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_JOB_STAGE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_JOB_STATUS = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_JOB_TIMEOUT = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_JOB_TOKEN = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_JOB_URL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_JOB_STARTED_AT = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_KUBERNETES_ACTIVE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_NODE_INDEX = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_NODE_TOTAL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_OPEN_MERGE_REQUESTS = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PAGES_DOMAIN = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PAGES_URL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PIPELINE_ID = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PIPELINE_IID = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PIPELINE_SOURCE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PIPELINE_TRIGGERED = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PIPELINE_URL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PIPELINE_CREATED_AT = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PIPELINE_NAME = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PROJECT_DIR = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PROJECT_ID = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PROJECT_NAME = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PROJECT_NAMESPACE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PROJECT_NAMESPACE_ID = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PROJECT_PATH_SLUG = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PROJECT_PATH = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PROJECT_REPOSITORY_LANGUAGES = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PROJECT_ROOT_NAMESPACE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PROJECT_TITLE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PROJECT_DESCRIPTION = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PROJECT_URL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PROJECT_VISIBILITY = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_PROJECT_CLASSIFICATION_LABEL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_REGISTRY = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_REGISTRY_IMAGE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_REGISTRY_PASSWORD = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_REGISTRY_USER = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_REPOSITORY_URL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_RUNNER_DESCRIPTION = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_RUNNER_EXECUTABLE_ARCH = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_RUNNER_ID = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_RUNNER_REVISION = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_RUNNER_SHORT_TOKEN = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_RUNNER_TAGS = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_RUNNER_VERSION = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER_FQDN = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER_HOST = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER_NAME = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER_PORT = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER_PROTOCOL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER_SHELL_SSH_HOST = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER_SHELL_SSH_PORT = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER_REVISION = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER_TLS_CA_FILE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER_TLS_CERT_FILE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER_TLS_KEY_FILE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER_URL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER_VERSION_MAJOR = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER_VERSION_MINOR = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER_VERSION_PATCH = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER_VERSION = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SERVER = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_SHARED_ENVIRONMENT = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_TEMPLATE_REGISTRY_HOST = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    GITLAB_CI = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    GITLAB_FEATURES = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    GITLAB_USER_EMAIL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    GITLAB_USER_ID = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    GITLAB_USER_LOGIN = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    GITLAB_USER_NAME = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    KUBECONFIG = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    TRIGGER_PAYLOAD = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_APPROVED = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_ASSIGNEES = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_DIFF_BASE_SHA = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_DIFF_ID = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_EVENT_TYPE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_DESCRIPTION = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_DESCRIPTION_IS_TRUNCATED = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_ID = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_IID = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_LABELS = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_MILESTONE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_PROJECT_ID = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_PROJECT_PATH = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_PROJECT_URL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_REF_PATH = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_SOURCE_BRANCH_NAME = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_SOURCE_BRANCH_PROTECTED = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_SOURCE_BRANCH_SHA = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_SOURCE_PROJECT_ID = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_SOURCE_PROJECT_PATH = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_SOURCE_PROJECT_URL = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_SQUASH_ON_MERGE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_TARGET_BRANCH_NAME = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_TARGET_BRANCH_PROTECTED = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_TARGET_BRANCH_SHA = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_MERGE_REQUEST_TITLE = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_EXTERNAL_PULL_REQUEST_IID = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_EXTERNAL_PULL_REQUEST_SOURCE_REPOSITORY = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_EXTERNAL_PULL_REQUEST_TARGET_REPOSITORY = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_EXTERNAL_PULL_REQUEST_SOURCE_BRANCH_NAME = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_EXTERNAL_PULL_REQUEST_SOURCE_BRANCH_SHA = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_EXTERNAL_PULL_REQUEST_TARGET_BRANCH_NAME = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
    CI_EXTERNAL_PULL_REQUEST_TARGET_BRANCH_SHA = enum.auto()
    """https://docs.gitlab.com/ee/ci/variables/predefined_variables.html"""
