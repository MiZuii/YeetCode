class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """

        ttemp = [0 for _ in range(123 - 97)]

        # cocnvert stickerst to tab of tabs
        for i in range(len(stickers)):
            curr = stickers[i]
            # the range of small letters in ascii is 97 - 122
            temp = [0 for _ in range(123 - 97)]
            for letter in curr:
                temp[ord(letter) - 97] += 1
            stickers[i] = temp

        # convert target

        for letter in target:
            ttemp[ord(letter) - 97] += 1

        target = ttemp

        ans = 0

        # count and substract the stickers that must be in target
        for i in range(len(target)):
            first_ap = 0
            apper = 0
            for j in range(len(stickers)):
                if target[i] != 0 and stickers[j][i] != 0:
                    apper += 1
                    first_ap = j

            if apper == 0 and target[i] != 0:
                return -1
            elif apper == 1:
                ans += 1
                for i in range(123 - 97):
                    if target[i] != 0 and stickers[first_ap][i] != 0:
                        target[i] -= stickers[first_ap][i]
                        if target[i] < 0:
                            target[i] = 0

        while True:

            # check if the target is empty
            flag = True  # False means the target is not empty
            for i in range(len(target)):
                if target[i] != 0:
                    flag = False

            if flag:
                return ans

            ans += 1

            comp = [0, 0]
            for i in range(len(stickers)):
                curr = stickers[i]

                # check max compatibilyty
                temp = [0, i]
                for i in range(123 - 97):
                    if target[i] != 0 and curr[i] != 0:
                        temp[0] += 1

                if temp[0] > comp[0]:
                    comp = temp

            # delete the choosen sticker letters from the target
            for i in range(123 - 97):
                if target[i] != 0 and stickers[comp[1]] != 0:
                    target[i] -= stickers[comp[1]][i]
                    if target[i] < 0:
                        target[i] = 0