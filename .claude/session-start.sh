#!/bin/bash
# Session Start Hook — Claude Code 모바일/웹 환경 자동 세팅
set -e

echo "=== Chess Editor: 환경 세팅 ==="

# specify-cli 설치 (없을 경우)
if ! command -v specify &> /dev/null; then
  echo "specify-cli 설치 중..."
  uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
  echo "specify-cli 설치 완료"
fi

# 프로젝트 의존성 설치
echo "의존성 설치 중..."
uv sync

echo ""
echo "=== 현재 스펙 현황 ==="
SPECS_DIR=".specify/specs"
if [ -d "$SPECS_DIR" ] && [ "$(ls -A "$SPECS_DIR" 2>/dev/null)" ]; then
  ls "$SPECS_DIR"/*.md 2>/dev/null | xargs -I{} basename {} || echo "(스펙 없음)"
else
  echo "(스펙 없음 — /speckit.specify 로 새 스펙 시작)"
fi

echo ""
echo "=== 준비 완료 ==="
echo "스펙드리븐 개발 워크플로우: CLAUDE.md 참조"
