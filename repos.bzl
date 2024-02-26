def _impl(repository_ctx):
    repository_ctx.symlink(repository_ctx.attr.path, "")

local_repository = repository_rule(
    implementation = _impl,
)
