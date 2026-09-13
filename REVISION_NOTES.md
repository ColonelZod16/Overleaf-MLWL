# Paper revision notes

This branch (`paper-revisions-sep13`) contains the requested manuscript revisions grounded in the MLF_RE implementation and the supplied reference papers.

Key changes:
- aggregate communication QoS justification plus individual near/far-user constraints;
- explicit definitions/references for beamformers `w` and RIS amplitude `beta`;
- implementation-accurate first-order MAML/phase-adaptation description;
- convergence discussion and online prediction complexity;
- complete simulation/channel parameter table from the MATLAB/Python sources;
- regenerated RIS-size and power-sweep figures, with dashed no-RIS baselines;
- EPS + JPG exports for the regenerated figures.

The legacy ablation `qany` metric in the source code counts aggregate communication and sensing violations; it does not include individual-user floor violations. The paper states this explicitly.
