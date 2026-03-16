# Chess Editor Constitution

## Core Principles

### Terminal-First
모든 UI는 터미널 환경에서 동작해야 한다. Rich 라이브러리를 활용하여 아름답고 기능적인 TUI를 제공한다.

### Spec-Driven Development
구현 전에 반드시 스펙을 작성한다. 스펙은 사용자 관점에서 "무엇을"/"왜"를 기술하며, "어떻게"는 plan.md에서 다룬다.

### Simplicity First
가장 단순한 해결책을 먼저 시도한다. 불필요한 추상화, 조기 최적화, 과도한 설계를 피한다.

### Chess Standards Compliance
FEN 형식, 표준 체스 규칙, 유니코드 체스 기호 등 기존 체스 표준을 준수한다.

### Python Idioms
Python 3.13+ 기능을 활용하고 타입 힌트를 사용한다. uv로 의존성을 관리한다.

## Development Workflow

새 기능 개발 순서:
1. `.specify/specs/` 에 스펙 파일 작성
2. `.specify/specs/` 에 플랜 파일 작성
3. `.specify/specs/` 에 태스크 파일 작성
4. 태스크 순서대로 구현

## Tech Stack

- **언어**: Python 3.13+
- **패키지 관리**: uv
- **TUI**: Rich
- **테스트**: pytest (향후 추가 예정)

## Governance

이 헌법은 프로젝트의 모든 기술적 결정의 기준이 된다. 변경 시 버전을 업데이트한다.

**Version**: 1.0.0 | **Ratified**: 2026-03-16 | **Last Amended**: 2026-03-16
