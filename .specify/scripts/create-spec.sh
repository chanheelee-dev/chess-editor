#!/bin/bash
# create-spec.sh: 새 스펙 파일 세트 생성
# Usage: ./create-spec.sh <feature-name>

set -e

if [ -z "$1" ]; then
  echo "Usage: $0 <feature-name>"
  echo "Example: $0 fen-support"
  exit 1
fi

FEATURE="$1"
DATE=$(date +%Y-%m-%d)
SPECS_DIR="$(dirname "$0")/../specs"
TEMPLATES_DIR="$(dirname "$0")/../templates"

# 다음 번호 자동 결정
NEXT_NUM=$(ls "$SPECS_DIR"/*.md 2>/dev/null | grep -E "^[0-9]+" | wc -l)
NEXT_NUM=$(printf "%02d" $((NEXT_NUM + 1)))

SPEC_FILE="$SPECS_DIR/${NEXT_NUM}-${FEATURE}.md"
PLAN_FILE="$SPECS_DIR/${NEXT_NUM}-${FEATURE}-plan.md"
TASKS_FILE="$SPECS_DIR/${NEXT_NUM}-${FEATURE}-tasks.md"

# 스펙 파일 생성
cp "$TEMPLATES_DIR/spec-template.md" "$SPEC_FILE"
sed -i "s/\[FEATURE_NAME\]/$FEATURE/g" "$SPEC_FILE"
sed -i "s/\[DATE\]/$DATE/g" "$SPEC_FILE"
sed -i "s/\[BRANCH_NAME\]/feat\/$FEATURE/g" "$SPEC_FILE"

echo "Created: $SPEC_FILE"
echo ""
echo "Next steps:"
echo "1. Edit $SPEC_FILE"
echo "2. Create plan: cp $TEMPLATES_DIR/plan-template.md $PLAN_FILE"
echo "3. Create tasks: cp $TEMPLATES_DIR/tasks-template.md $TASKS_FILE"
