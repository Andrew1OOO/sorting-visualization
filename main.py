from sorting import Sorting
import pygame, random


pygame.init()
dis=pygame.display.set_mode((800,600))
dis.fill((51, 54, 56))
game_over=False
clock = pygame.time.Clock()
pygame.display.set_caption('Sorting Visualization')


def generate_random_list(size):
    list1 = []
    for i in range(size):
        list1.append(random.randint(50,470))
    return list1

def scramble(arr):
    dest = arr[:]
    random.shuffle(dest)
    return dest

x=random.randint(10,500)

list1 = generate_random_list(x)
sort = Sorting(list1,dis,50,480)

bSortButton = pygame.Rect(60, 530, 100, 40)
qSortButton = pygame.Rect(180, 530, 100, 40)
iSortButton = pygame.Rect(300, 530, 100, 40)

bdraw = True
qdraw = True
idraw = True

Font = pygame.freetype.SysFont('Sans', 16)





while not game_over:
    dis.fill((51, 54, 56))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_l:
                x=random.randint(250,500)
                list1 = generate_random_list(x)
                sort = Sorting(list1,dis,50,480)
            if event.key == pygame.K_m:
                x=random.randint(75,250)
                list1 = generate_random_list(x)
                sort = Sorting(list1,dis,50,480)
            if event.key == pygame.K_s:
                x=random.randint(10,75)
                list1 = generate_random_list(x)
                sort = Sorting(list1,dis,50,480)
            
            if event.key == pygame.K_c:
                list1 = scramble(list1)
                sort = Sorting(list1,dis,50,480)
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            if bSortButton.collidepoint(pos):
                
                bdraw = False
            if qSortButton.collidepoint(pos):
                
                qdraw = False
            if iSortButton.collidepoint(pos):
                
                idraw = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if bSortButton.collidepoint(pos):
                sort.bubble_sort()
                bdraw = True
            if qSortButton.collidepoint(pos):
                sort.quick_sort(0,x-1)
                qdraw = True
            if iSortButton.collidepoint(pos):
                sort.insertionSort()
                idraw = True

    sort.paint()


    
    
    if(bdraw):
        pygame.draw.rect(dis,(149, 48, 217),bSortButton)
    else:
        pygame.draw.rect(dis,(128, 38, 189),bSortButton)
    if(qdraw):
        pygame.draw.rect(dis,(149, 48, 217),qSortButton)
    else:
        pygame.draw.rect(dis,(128, 38, 189),qSortButton)
    if(idraw):
        pygame.draw.rect(dis,(149, 48, 217),iSortButton)
    else:
        pygame.draw.rect(dis,(128, 38, 189),iSortButton)


    
    bubble_rect = Font.get_rect("Bubble Sort")
    bwidth = bubble_rect.width
    bheight = bubble_rect.height
    bubble_rect.center = ((60+(100-bwidth)/2),(530+(40-bheight)/2))
    bubbled = Font.render_to(dis, bubble_rect.center, "Bubble Sort", (0,0,0))

    

    quick_rect = Font.get_rect("Quick Sort")
    qwidth = quick_rect.width
    qheight = quick_rect.height
    quick_rect.center = ((180+(100-qwidth)/2),(530+(40-qheight)/2))
    quicked = Font.render_to(dis, quick_rect.center, "Quick Sort", (0,0,0))


    insertion_rect = Font.get_rect("Insertion Sort")
    iwidth = insertion_rect.width
    iheight = insertion_rect.height
    insertion_rect.center = ((300+(100-iwidth)/2),(530+(40-iheight)/2))
    inserted = Font.render_to(dis, insertion_rect.center, "Insertion Sort", (0,0,0))


    pygame.display.update()
    pygame.display.flip()




    clock.tick(120)
pygame.quit()
quit()