#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <unistd.h>

void transfer_files(const char *source_dir, const char *destination_dir) {
    DIR *source_dp, *destination_dp;
    struct dirent *entry;
    char source_path[1024];
    char destination_path[1024];

    source_dp = opendir(source_dir);
    if (source_dp == NULL) {
        perror("Impossible d'ouvrir le répertoire source");
        exit(EXIT_FAILURE);
    }
    if (access(destination_dir, F_OK) == -1) {
        
        perror("Impossible de joindre le répertoire destination");
        exit(EXIT_FAILURE);
    }
    destination_dp = opendir(destination_dir);
    if (destination_dp == NULL) {
        perror("Impossible d'ouvrir le répertoire destination");
        exit(EXIT_FAILURE);
    }
    while ((entry = readdir(source_dp)) != NULL) {
        if (strcmp(entry->d_name, ".") != 0 && strcmp(entry->d_name, "..") != 0) {
            sprintf(source_path, "%s/%s", source_dir, entry->d_name);
            sprintf(destination_path, "%s/%s", destination_dir, entry->d_name);
            if (rename(source_path, destination_path) != 0) {
                perror("Erreur lors du transfert du fichier");
            } else {
                printf("Fichier '%s' transféré avec succès de '%s' vers '%s'\n", entry->d_name, source_dir, destination_dir);
            }
        }
    }
    closedir(source_dp);
    closedir(destination_dp);
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Utilisation: %s <source_dir> <destination_dir>\n", argv[0]);
        return EXIT_FAILURE;
    }
    transfer_files(argv[1], argv[2]);
    return EXIT_SUCCESS;
}
