1. Whenever there is a file "plan.md" always follow the plan.
2. When a point of a plan is completed, mark it as finished in plan.md
3. When you need to work with a library/framework use context7 to check if your usage is correct
4. When you need to add a dependency to project - check the latest version at context7
5. Do NOT add `quarkus-resteasy-reactive-multipart`; in Quarkus 3, multipart APIs (`@RestForm`, `FileUpload`) are available via `quarkus-rest` already.
6. To test how fb2c works, you can execute "/home/finkel/Downloads/fb2c-linux-amd64/fb2c" binary
