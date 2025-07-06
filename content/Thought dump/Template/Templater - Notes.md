<%*
const rootFolder = "content"; // Vault 내부 상대 경로
const outputPath = `${rootFolder}/Thought dump/Template/Notes.md`; // 저장할 파일 경로

async function generateNotes() {
    try {
        // 1️⃣ **모든 Markdown 파일 가져오기 (루트 폴더 제외)**
        const allFiles = app.vault.getFiles()
            .filter(file => file.path.startsWith(rootFolder + "/") && file.extension === "md")
            .filter(file => file.path.split("/").length > 2)
            .map(file => {
                const fileCache = app.metadataCache.getCache(file.path) || {};
                const frontmatter = fileCache.frontmatter || {};
                const title = frontmatter.title ? String(frontmatter.title) : file.basename; // title이 없으면 file.basename 사용
                
                return {
                    name: file.basename,
                    title: title || file.basename, // title이 없으면 file.basename을 기본값으로
                    path: file.path
                };
            });

        // 2️⃣ **정리할 파일이 없는 경우 빈 파일 생성**
        if (allFiles.length === 0) {
            await app.vault.adapter.write(outputPath, "---\npublished: \"false\"\n---\n\n");
            new Notice(`✅ 빈 파일 생성 완료: ${outputPath}`);
            return;
        }

        // 3️⃣ **모든 폴더 및 하위 폴더 목록을 정리 (가나다순)**
        const folderMap = {};

        allFiles.forEach(file => {
            const parts = file.path.split("/");
            if (parts.length < 3) return;

            const folder = parts[1];
            const subFolder = parts.length > 3 ? parts[2] : null;

            if (!folderMap[folder]) folderMap[folder] = { files: [], subFolders: {} };
            if (subFolder) {
                if (!folderMap[folder].subFolders[subFolder]) folderMap[folder].subFolders[subFolder] = [];
                folderMap[folder].subFolders[subFolder].push(file);
            } else {
                folderMap[folder].files.push(file);
            }
        });

        // 4️⃣ **폴더 및 하위 폴더 정렬 (가나다순)**
        const sortedFolders = Object.keys(folderMap).sort((a, b) => a.localeCompare(b, "ko-KR"));

        // 5️⃣ **파일 목록 생성**
        let content = "";

        for (const folder of sortedFolders) {
            content += `## ${folder}\n`;

            let topLevelFiles = folderMap[folder].files.sort((a, b) => (a.title || a.name).localeCompare(b.title || b.name, "ko-KR"));

            for (const file of topLevelFiles) {
                content += `- [[${file.name} | ${file.title}]]\n`;
            }

            let sortedSubFolders = Object.keys(folderMap[folder].subFolders).sort((a, b) => a.localeCompare(b, "ko-KR"));

            for (const subFolder of sortedSubFolders) {
                content += `\n### ${subFolder}\n`;

                let subFolderFiles = folderMap[folder].subFolders[subFolder].sort((a, b) => (a.title || a.name).localeCompare(b.title || b.name, "ko-KR"));

                for (const file of subFolderFiles) {
                    content += `- [[${file.name} | ${file.title}]]\n`;
                }
            }

            content += "\n";
        }

        // 6️⃣ **파일 무조건 덮어쓰기**
        await app.vault.adapter.write(outputPath, content);
        new Notice(`✅ 파일 생성 완료: ${outputPath}`);

    } catch (error) {
        new Notice(`⚠️ 오류 발생: ${error.message}`);
        console.error(error);
    }
}

// 비동기 실행
generateNotes();
%>

