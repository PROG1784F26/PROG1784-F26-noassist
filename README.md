# PROG1784-F26-noassist

Python course workspace based on
[PROG1784F26/PROG1784-F26](https://github.com/PROG1784F26/PROG1784-F26),
with AI writing suggestions disabled and Continue removed.

A single Python 3.13 container provides Python, Pylance, debugging, Ruff, and
pytest. The terminal, debugger, and editor use `/home/vscode/.venv`.
The project has no AI model downloads or background AI services.

## Setup walkthrough

**Host terminal** means your computer. **Container terminal** means the terminal
after reopening this checkout in its devcontainer. Run commands from the
repository root unless a step says otherwise.

### 1. Install and start a container engine

**Docker is the default.** Choose one engine; installing both is unnecessary.
**Already using Podman?** With a working Docker-compatible CLI and Compose,
the unchanged repository uses Podman: no VS Code or repository edits are needed.
Follow [Podman with no repository changes](.devcontainer/CONTAINER_ENGINE.md#podman-with-no-repository-changes)
for Linux packages, Podman Desktop setup, and the checks to run before `code .`.
Installing Podman alone is insufficient; the compatibility command must exist
and point to its engine. A separate [direct Podman option](.devcontainer/CONTAINER_ENGINE.md#alternative-select-podman-explicitly)
is documented for users who prefer to change VS Code and the startup hook.

| Your computer | Docker route | Podman route |
| --- | --- | --- |
| Linux | Install Docker Engine and Compose v2 for your distribution; allow your user to run Docker without `sudo` | Install Podman 5+, a Compose provider, and Docker CLI compatibility; distribution packages commonly include `podman-docker` and `podman-compose` |
| macOS, Intel or Apple Silicon | Install the matching Docker Desktop build and start it | Install Podman Desktop, create/start its Linux machine, configure Compose and Docker compatibility |
| Windows | Install Docker Desktop with the WSL2 backend, use Linux containers, and enable integration for your WSL distribution if using one | Install Podman Desktop, create/start its Linux machine, configure Compose and Docker compatibility |

Use the official [Docker installation instructions](https://docs.docker.com/get-started/get-docker/)
or [Podman Desktop installation instructions](https://podman-desktop.io/docs/installation).
For Podman Desktop, also follow its [Compose setup](https://podman-desktop.io/docs/compose/setting-up-compose)
and [Docker compatibility setup](https://podman-desktop.io/docs/migrating-from-docker/managing-docker-compatibility).
Podman alone is not enough for this Compose-based devcontainer. A shell alias such
as `alias docker=podman` is insufficient because VS Code launches an executable.

On Windows, keeping the checkout in your WSL Linux home gives better filesystem
performance. Open that folder with VS Code's WSL extension, then reopen it in the
devcontainer. Check engine access from that same WSL environment. If working
from a Windows folder instead, ensure the engine can share that folder. On
macOS, allow the container VM access to the checkout when prompted.

**Host terminal, from any folder** — for the default Docker or Docker-compatible
route, check the engine before continuing:

```text
docker info
docker compose version
```

Both commands must succeed. `docker info` must reach the running engine; seeing
only a Docker client version is not enough. A Podman compatibility notice is
normal. If either command fails, start the engine/machine and finish its CLI or
Compose setup before opening the devcontainer. In VS Code, leave **Dev Containers:
Docker Path** set to `docker` for this route. For direct Podman, use the linked
switch instructions and verify `podman info` / `podman compose version` instead.

### 2. Install VS Code and get the course repository

#### Install the VS Code desktop application

1. Open the [VS Code download page](https://code.visualstudio.com/download).
2. Choose your operating system and computer architecture (x64 or ARM64).
3. Install and launch the application using the appropriate route below.

| Operating system | Installation |
| --- | --- |
| Windows | Run the downloaded installer and follow its prompts. For the WSL workflow, install the VS Code desktop application on Windows. |
| macOS | Open the downloaded installer/archive, move Visual Studio Code into Applications, and launch it from there. |
| Linux | Install the package appropriate for your distribution, such as `.deb` for Ubuntu/Debian or `.rpm` for Fedora/RHEL, then launch VS Code. |

See Microsoft's [VS Code installation guide](https://code.visualstudio.com/docs/getstarted/overview#install-vs-code)
for platform-specific details. To use `code .` from a macOS terminal, open the
Command Palette and run **Shell Command: Install 'code' command in PATH**.
Reopen the terminal after changing PATH. Opening the folder through VS Code's
File menu also works.

#### Install the required VS Code extensions

VS Code calls its plugins **extensions**. Install these host extensions before
reopening the repository in its container:

1. In VS Code, open **View → Extensions**, or press **Ctrl+Shift+X** on
   Linux/Windows or **Cmd+Shift+X** on macOS.
2. Search for `ms-vscode-remote.remote-containers`.
3. Select **Dev Containers** by **Microsoft** and click **Install**.
4. If using a WSL checkout on Windows, also search for
   `ms-vscode-remote.remote-wsl` and install **WSL** by **Microsoft** in the
   Windows VS Code application. Follow the [VS Code WSL guide](https://code.visualstudio.com/docs/remote/wsl)
   to open your Linux folder before reopening it in the devcontainer.
5. Reload VS Code if prompted. In the Command Palette, confirm
   **Dev Containers: Reopen in Container** is available once the course folder
   is open.

For more detail, see [installing VS Code extensions](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace).

When you reopen this repository in its devcontainer, the project automatically
requests these additional extensions **inside the container**:

| Extension | Extension ID | Purpose |
| --- | --- | --- |
| Python | `ms-python.python` | Interpreter selection, running Python, and test integration |
| Pylance | `ms-python.vscode-pylance` | Python completion and type analysis |
| Python Debugger | `ms-python.debugpy` | The configured F5 debugger |
| Ruff | `charliermarsh.ruff` | Python linting and formatting |

After step 3 below, return to **Extensions** and check the installed extensions
for the **Dev Container**. If an automatic installation failed, search for the
exact ID above and choose **Install in Dev Container** while connected. A copy
installed only under **Local** does not confirm the container copy is installed.

#### Install Git and open the repository

Install [Git](https://git-scm.com/downloads) in the environment where you will
clone; for the WSL workflow, Git must also be available inside that WSL distribution.

The course repository is [PROG1784F26/PROG1784-F26-noassist](https://github.com/PROG1784F26/PROG1784-F26-noassist).
Run the clone command from the directory where you keep your course folders.
If your instructor assigns a personal fork or a different repository, substitute
that repository URL.

**Host terminal:**

```text
git --version
git clone https://github.com/PROG1784F26/PROG1784-F26-noassist.git PROG1784-F26-noassist
cd PROG1784-F26-noassist
code .
```

If you already have this checkout, open it rather than cloning again. If `code`
is not on your PATH, use **File: Open Folder** in VS Code and select
`PROG1784-F26-noassist`. Open the repository root containing `.devcontainer`
and `examples`, not just its parent or `examples` folder.

Keep the visible course folder named **PROG1784-F26-noassist**. Internal container/project
names use lowercase for engine compatibility; there is nothing to rename there.
No host Python or Node.js installation is required for this setup.

### 3. Reopen the folder in its devcontainer

Open the Command Palette with **F1**, **Ctrl+Shift+P** on Linux/Windows, or
**Cmd+Shift+P** on macOS. Run **Dev Containers: Reopen in Container**.
Startup configures Docker/Podman permissions, builds the Python image, and
installs the Python extensions. First startup needs internet access for the
image, Python packages, and extensions.

The remote indicator should show **PROG1784-F26-noassist Python**. Your checkout
is mounted at `/workspaces/PROG1784-F26-noassist` inside the container; edits
are saved in your host checkout.

### 4. Check Python

**Container terminal:**

```sh
python --version
python examples/hello.py
python .devcontainer/smoke.py
ruff check .
```

Python should report 3.13. The smoke check verifies the interpreter, non-root
workspace writes, and virtual environment permissions.

### 5. Write, run, and debug

Open `examples/hello.py` and press **F5** for the debugger. Use **Terminal: Run
Task** to run the current file, pytest, Ruff checks, or formatting. Pylance
provides normal Python completion menus and type analysis. Ruff formats on save.

Add `test_*.py` files and run `python -m pytest`, or use the Testing sidebar.
The starter has no assignment tests, so pytest reports no tests until you add
some. Container setup tests run with
`python -m unittest discover -s .devcontainer/tests -v`.

## AI suggestions

Workspace and container settings disable inline suggestions, completion
previews, Copilot automatic completions, next-edit suggestions, and automatic
rename suggestions. `chat.disableAIFeatures` also disables VS Code's built-in AI
features and Copilot extensions. See the official
[VS Code AI settings reference](https://code.visualstudio.com/docs/agents/reference/ai-settings).

Continue is removed from extension installation and marked as an unwanted
recommendation alongside Copilot. There is no Continue config, Ollama service,
tutor adapter, or model provisioning task.

For an environment created before this change, run **Dev Containers: Rebuild
Container**. If Continue is installed in your host VS Code profile, open its
extension gear and choose **Disable (Workspace)** for this checkout. Repository
recommendations do not uninstall extensions already in a host profile.

These are repository defaults; language-specific user settings and extensions
in other editors can require separate configuration.

## Daily use and dependencies

Start the container engine, open this checkout in VS Code, and reopen it in its
devcontainer. Closing the window stops the Python service. Files remain in your
host checkout across stops and rebuilds.

Add dependencies to `requirements-dev.txt` and rebuild the container. Packages
installed only in a running container can be lost during rebuilds.

## Docker and Podman

Docker is the default. A working Docker-compatible CLI connected to Podman
works without repository changes. See the
[engine guide](.devcontainer/CONTAINER_ENGINE.md) for compatibility setup,
direct Podman configuration, and switching engines.

The Compose project name is `prog1784f26noassist`, separate from the original
repository's `prog1784f26`. Use one active checkout of this variant per engine
to avoid reusing a container with an old host mount.

For manual startup, generate the runtime override first. **Host terminal**:

```sh
docker run --rm --user 0 --volume "/absolute/path/PROG1784-F26-noassist/.devcontainer:/config:z" mcr.microsoft.com/devcontainers/python:1-3.13-bookworm python /config/configure_runtime.py
docker compose -f .devcontainer/compose.yaml -f .devcontainer/compose.runtime.yaml up -d --build
```

Substitute your absolute checkout path. Use both Compose files so Podman gets
the runtime user mapping when needed.

## Troubleshooting and stopping

- **Engine unavailable:** check `docker info` and `docker compose version` in
  the host environment that opens VS Code. Start the engine first.
- **Old checkout path in an error:** close the devcontainer, run
  `docker compose -f .devcontainer/compose.yaml down`, then reopen it.
- **Permission denied with rootless Podman:** rebuild so the startup probe
  regenerates `.devcontainer/compose.runtime.yaml`.
- **Wrong interpreter:** select `/home/vscode/.venv/bin/python` in VS Code and
  confirm the window is connected to the devcontainer.
- **Logs:** `docker compose -f .devcontainer/compose.yaml logs --tail=100 python`.
- **Stop:** `docker compose -f .devcontainer/compose.yaml stop`.
- **Remove containers:** `docker compose -f .devcontainer/compose.yaml down`.

## Validation

CI runs runtime tests and Ruff checks on Linux, macOS, and Windows. Its Linux
container job starts the devcontainer, checks its interpreter and writable
workspace, and runs the example. Desktop UI workflows on macOS and Windows
still need interactive verification.
