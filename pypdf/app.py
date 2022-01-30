import PyPDF2

with open('cv.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('rotated.pdf', 'wb') as output:
        writer.write(output)

    print('Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, molestias nobis omnis adipisci quis fugit pariatur, architecto hic iste porro numquam ipsum! Veniam odit laborum vel dolores voluptate nesciunt pariatur quaerat, enim hic nobis dolore aspernatur blanditiis ad, neque vero culpa, suscipit optio! Minus, autem, voluptates magni excepturi harum repellat aspernatur odio dolor nihil iste ducimus accusamus beatae ab ullam exercitationem libero ipsum, architecto suscipit quos adipisci? Harum officiis non laboriosam saepe tenetur repellat, incidunt, veritatis, obcaecati explicabo adipisci ipsum sint minima accusantium sapiente voluptatem. Vero maxime nesciunt nemo commodi obcaecati quidem perferendis non voluptatibus cumque? Quibusdam hic pariatur ea beatae natus dolor minima dicta nobis modi quos aliquid doloribus minus praesentium aspernatur quidem, optio facilis maiores rerum esse odit eaque. Omnis recusandae a neque alias error ut, voluptas, ducimus amet provident dignissimos officia inventore quaerat odit. Cupiditate saepe fugit sed quaerat velit, dicta ab accusantium error nemo. Dolor, facilis laudantium sint voluptatibus, adipisci quod cumque autem vero veritatis nemo consequatur neque libero culpa. Dolor, aut accusantium. In aliquid molestiae perspiciatis vero commodi dolores adipisci, aspernatur expedita atque odio molestias. Sit sunt natus molestias voluptatum aliquam maxime vel, consequuntur beatae temporibus magnam, distinctio voluptate commodi tenetur atque hic autem explicabo repellat nihil similique! Eaque odit, commodi perspiciatis, corrupti consequuntur expedita libero exercitationem, blanditiis itaque esse similique modi alias enim perferendis delectus laboriosam nostrum voluptatem officiis? Totam, neque sint. Repudiandae quo voluptatem voluptates inventore, nostrum vitae consectetur ea! Minus perspiciatis magni, sed cumque libero, quisquam dolorem nemo, voluptatum expedita officiis dolores! Aspernatur amet, numquam quo facilis fugiat modi illum voluptatum dolor! Dolor soluta temporibus, necessitatibus maxime mollitia illo ex earum facere. Blanditiis illum, iure vel quaerat quod quis libero culpa ut, veniam perspiciatis minima nemo incidunt nisi commodi. Voluptas facilis, atque eaque natus, laborum officia tempora, cupiditate fugit provident quos earum vel blanditiis. Deserunt, architecto odit, culpa doloribus fugiat alias quam cumque, porro ea facilis nihil adipisci explicabo ratione aliquid cupiditate impedit eos recusandae eveniet tempore harum. Beatae dolorum officia assumenda veritatis vitae numquam, quidem deserunt minus, sint enim eius laudantium, alias doloremque officiis exercitationem rem neque fugit! Perspiciatis assumenda, corrupti, eaque est commodi, et nobis recusandae enim eum architecto animi dolores unde quia harum temporibus reiciendis accusantium cum quis? Natus, doloremque magni. Maxime possimus illo debitis architecto magni fugit aliquam ex nostrum, ea facere obcaecati dolorum reiciendis eos odit sapiente pariatur. Aspernatur quidem officia culpa libero possimus excepturi, ab inventore qui nihil tenetur impedit fuga illo ut reiciendis blanditiis. Commodi earum repellat necessitatibus perferendis quod aliquid, ut incidunt deserunt itaque qui vel, pariatur facilis voluptas repellendus aliquam quaerat eos cum et nisi harum, doloremque tempore atque tenetur. Consequuntur delectus, sed vitae asperiores quod natus quo numquam libero dolor eius et necessitatibus quasi enim assumenda ducimus repudiandae blanditiis, sequi quia nihil? Adipisci culpa sed voluptatem, incidunt officiis fugit doloremque recusandae quo eos maxime magni doloribus blanditiis cupiditate, atque animi nesciunt sit voluptas sint? Iure reiciendis debitis corrupti magnam explicabo, similique tenetur illo laborum labore nulla porro deserunt distinctio illum adipisci consectetur.')
    print('Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, molestias nobis omnis adipisci quis fugit pariatur, architecto hic iste porro numquam ipsum! Veniam odit laborum vel dolores voluptate nesciunt pariatur quaerat, enim hic nobis dolore aspernatur blanditiis ad, neque vero culpa, suscipit optio! Minus, autem, voluptates magni excepturi harum repellat aspernatur odio dolor nihil iste ducimus accusamus beatae ab ullam exercitationem libero ipsum, architecto suscipit quos adipisci? Harum officiis non laboriosam saepe tenetur repellat, incidunt, veritatis, obcaecati explicabo adipisci ipsum sint minima accusantium sapiente voluptatem. Vero maxime nesciunt nemo commodi obcaecati quidem perferendis non voluptatibus cumque? Quibusdam hic pariatur ea beatae natus dolor minima dicta nobis modi quos aliquid doloribus minus praesentium aspernatur quidem, optio facilis maiores rerum esse odit eaque. Omnis recusandae a neque alias error ut, voluptas, ducimus amet provident dignissimos officia inventore quaerat odit. Cupiditate saepe fugit sed quaerat velit, dicta ab accusantium error nemo. Dolor, facilis laudantium sint voluptatibus, adipisci quod cumque autem vero veritatis nemo consequatur neque libero culpa. Dolor, aut accusantium. In aliquid molestiae perspiciatis vero commodi dolores adipisci, aspernatur expedita atque odio molestias. Sit sunt natus molestias voluptatum aliquam maxime vel, consequuntur beatae temporibus magnam, distinctio voluptate commodi tenetur atque hic autem explicabo repellat nihil similique! Eaque odit, commodi perspiciatis, corrupti consequuntur expedita libero exercitationem, blanditiis itaque esse similique modi alias enim perferendis delectus laboriosam nostrum voluptatem officiis? Totam, neque sint. Repudiandae quo voluptatem voluptates inventore, nostrum vitae consectetur ea! Minus perspiciatis magni, sed cumque libero, quisquam dolorem nemo, voluptatum expedita officiis dolores! Aspernatur amet, numquam quo facilis fugiat modi illum voluptatum dolor! Dolor soluta temporibus, necessitatibus maxime mollitia illo ex earum facere. Blanditiis illum, iure vel quaerat quod quis libero culpa ut, veniam perspiciatis minima nemo incidunt nisi commodi. Voluptas facilis, atque eaque natus, laborum officia tempora, cupiditate fugit provident quos earum vel blanditiis. Deserunt, architecto odit, culpa doloribus fugiat alias quam cumque, porro ea facilis nihil adipisci explicabo ratione aliquid cupiditate impedit eos recusandae eveniet tempore harum. Beatae dolorum officia assumenda veritatis vitae numquam, quidem deserunt minus, sint enim eius laudantium, alias doloremque officiis exercitationem rem neque fugit! Perspiciatis assumenda, corrupti, eaque est commodi, et nobis recusandae enim eum architecto animi dolores unde quia harum temporibus reiciendis accusantium cum quis? Natus, doloremque magni. Maxime possimus illo debitis architecto magni fugit aliquam ex nostrum, ea facere obcaecati dolorum reiciendis eos odit sapiente pariatur. Aspernatur quidem officia culpa libero possimus excepturi, ab inventore qui nihil tenetur impedit fuga illo ut reiciendis blanditiis. Commodi earum repellat necessitatibus perferendis quod aliquid, ut incidunt deserunt itaque qui vel, pariatur facilis voluptas repellendus aliquam quaerat eos cum et nisi harum, doloremque tempore atque tenetur. Consequuntur delectus, sed vitae asperiores quod natus quo numquam libero dolor eius et necessitatibus quasi enim assumenda ducimus repudiandae blanditiis, sequi quia nihil? Adipisci culpa sed voluptatem, incidunt officiis fugit doloremque recusandae quo eos maxime magni doloribus blanditiis cupiditate, atque animi nesciunt sit voluptas sint? Iure reiciendis debitis corrupti magnam explicabo, similique tenetur illo laborum labore nulla porro deserunt distinctio illum adipisci consectetur.')
