package com.example.gradle;

import java.io.IOException;
import java.util.Set;
import java.io.File;
import java.nio.file.Files;
import java.util.Collections;
import org.gradle.api.DefaultTask;
import org.gradle.api.tasks.TaskAction;
import org.gradle.api.file.ConfigurableFileCollection;
import org.gradle.api.file.RegularFileProperty;
import org.gradle.api.tasks.InputFiles;
import org.gradle.api.tasks.OutputFile;

public abstract class CountJars extends DefaultTask {

    @InputFiles
    public abstract ConfigurableFileCollection getListJars();

    @OutputFile
    public abstract RegularFileProperty getResultFile();

    @TaskAction
    public void doCount() throws IOException {
        Set<File> fileSet = getListJars().getFiles();
        int count = fileSet.size();
        File out = getResultFile().get().getAsFile();
        Files.write(out.toPath(), Collections.singleton("" + count));
    }
}